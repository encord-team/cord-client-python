import platform
import uuid
from typing import Dict, Iterator, List, Optional, Sequence, Type, TypeVar, Union
from urllib.parse import urljoin

import requests
from requests import PreparedRequest, Response

from encord._version import __version__ as encord_version
from encord.configs import Config
from encord.exceptions import EncordException, RequestException
from encord.http.common import (
    HEADER_CLOUD_TRACE_CONTEXT,
    HEADER_USER_AGENT,
    RequestContext,
)
from encord.http.utils import create_new_session
from encord.http.v2.error_utils import handle_error_response
from encord.http.v2.payloads import Page
from encord.orm.base_dto import BaseDTO, BaseDTOInterface

T = TypeVar("T", bound=Union[BaseDTOInterface, uuid.UUID, int, str])


class ApiClient:
    def __init__(self, config: Config):
        self._config = config
        self._domain = self._config.domain
        self._base_path = "v2/public/"

    @staticmethod
    def _exception_context_from_response(response: Response) -> RequestContext:
        try:
            x_cloud_trace_context = response.headers.get(HEADER_CLOUD_TRACE_CONTEXT)
            if x_cloud_trace_context is None:
                return RequestContext()

            x_cloud_trace_context = x_cloud_trace_context.split(";")[0]
            trace_id, span_id = (x_cloud_trace_context.split("/") + [None, None])[:2]
            return RequestContext(trace_id=trace_id, span_id=span_id)
        except Exception:
            return RequestContext()

    @staticmethod
    def _exception_context(request: requests.PreparedRequest) -> RequestContext:
        try:
            x_cloud_trace_context = request.headers.get(HEADER_CLOUD_TRACE_CONTEXT)
            if x_cloud_trace_context is None:
                return RequestContext()

            x_cloud_trace_context = x_cloud_trace_context.split(";")[0]
            trace_id, span_id = (x_cloud_trace_context.split("/") + [None, None])[:2]
            return RequestContext(trace_id=trace_id, span_id=span_id)
        except Exception:
            return RequestContext()

    @staticmethod
    def _user_agent() -> str:
        return f"encord-sdk-python/{encord_version} python/{platform.python_version()}"

    @staticmethod
    def _tracing_id() -> str:
        return f"{uuid.uuid4().hex}/1;o=1"

    def _build_url(self, path: str) -> str:
        if path.startswith("/"):
            path = path[1:]
        url = urljoin(self._domain, urljoin(self._base_path, path))
        if url.endswith("/"):
            url = url[:-1]
        return url

    def _headers(self):
        return {
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "Content-Type": "application/json",
            HEADER_USER_AGENT: self._user_agent(),
            HEADER_CLOUD_TRACE_CONTEXT: self._tracing_id(),
        }

    def get(self, path: str, params: Optional[BaseDTO], result_type: Type[T], allow_none: bool = False) -> T:
        return self._request_without_payload("GET", path, params, result_type)

    def get_paged_iterator(
        self,
        path: str,
        params: BaseDTO,
        result_type: Type[T],
        allow_none: bool = False,
    ) -> Iterator[T]:
        if not hasattr(params, "page_token"):
            raise ValueError("params must have a page_token attribute for paging to work")

        while True:
            #  Pydantic is magic and relies on under-specified parts of the type system
            #  MyPy doesn't like this (insists on 'type erasure'), but it works because
            #  in reality the type is not erased and the generic parameters are available
            page = self.get(
                path,
                params=params,
                result_type=Page[result_type],  # type: ignore[valid-type]
                allow_none=allow_none,
            )

            yield from page.results

            if page.next_page_token is not None:
                params.page_token = page.next_page_token
            else:
                break

    def delete(self, path: str, params: Optional[BaseDTO], result_type: Optional[Type[T]] = None) -> T:
        return self._request_without_payload("DELETE", path, params, result_type)

    def post(
        self,
        path: str,
        params: Optional[BaseDTO],
        payload: Union[BaseDTO, Sequence[BaseDTO], None],
        result_type: Optional[Type[T]],
    ) -> T:
        return self._request_with_payload("POST", path, params, payload, result_type)

    def patch(
        self, path: str, params: Optional[BaseDTO], payload: Optional[BaseDTO], result_type: Optional[Type[T]]
    ) -> T:
        return self._request_with_payload("PATCH", path, params, payload, result_type)

    def _serialise_payload(self, payload: Union[BaseDTO, Sequence[BaseDTO], None]) -> Union[List[Dict], Dict, None]:
        if isinstance(payload, list):
            return [p.to_dict() for p in payload]
        elif isinstance(payload, BaseDTO):
            return payload.to_dict()
        elif payload is None:
            return None
        else:
            raise ValueError(f"Unsupported payload type: {type(payload)}")

    def _request_with_payload(
        self,
        method: str,
        path: str,
        params: Optional[BaseDTO],
        payload: Union[BaseDTO, Sequence[BaseDTO], None],
        result_type: Optional[Type[T]],
    ) -> T:
        params_dict = params.to_dict() if params is not None else None
        payload_serialised = self._serialise_payload(payload)

        req = requests.Request(
            method=method,
            url=self._build_url(path),
            headers=self._headers(),
            params=params_dict,
            json=payload_serialised,
        ).prepare()

        return self._request(req, result_type=result_type)  # type: ignore

    def _request_without_payload(
        self, method: str, path: str, params: Optional[BaseDTO], result_type: Optional[Type[T]]
    ) -> T:
        params_dict = params.to_dict() if params is not None else None

        req = requests.Request(
            method=method, url=self._build_url(path), headers=self._headers(), params=params_dict
        ).prepare()

        return self._request(req, result_type=result_type)  # type: ignore

    def _request(self, req: PreparedRequest, result_type: Optional[Type[T]], allow_none: bool = False):
        req = self._config.define_headers_v2(req)

        timeouts = (self._config.connect_timeout, self._config.read_timeout)
        req_settings = self._config.requests_settings
        with create_new_session(
            max_retries=req_settings.max_retries,
            backoff_factor=req_settings.backoff_factor,
            connect_retries=req_settings.connection_retries,
        ) as session:
            context = self._exception_context(req)

            res = session.send(req, timeout=timeouts)

            if res.status_code != 200:
                self._handle_error(res, context)

            try:
                res_json = res.json()
            except Exception as e:
                raise RequestException(f"Error parsing JSON response: {res.text}", context=context) from e

            if result_type is None or (res_json is None and allow_none):
                return None
            if result_type == int:
                return int(res_json)
            elif result_type == str:
                return str(res_json)
            elif result_type == uuid.UUID:
                return uuid.UUID(res_json)
            elif issubclass(result_type, BaseDTOInterface):
                return result_type.from_dict(res_json)
            else:
                raise ValueError(f"Unsupported result type {result_type}")

    @staticmethod
    def _handle_error(response: Response, context: RequestContext):
        try:
            description = response.json()
            handle_error_response(response.status_code, context=context, message=description.get("message"))
        except EncordException as e:
            raise e
        except Exception:
            handle_error_response(response.status_code, context=context)
