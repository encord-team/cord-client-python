import platform
from typing import Any, Dict, Optional
from urllib.parse import urljoin

import requests
from requests import Response
from requests.exceptions import JSONDecodeError

from encord._version import __version__ as encord_version
from encord.configs import UserConfig
from encord.exceptions import RequestException
from encord.http.common import (
    HEADER_CLOUD_TRACE_CONTEXT,
    HEADER_USER_AGENT,
    RequestContext,
)
from encord.http.utils import create_new_session
from encord.http.v2.request_signer import sign_request


class ApiClient:
    def __init__(self, config: UserConfig):
        self._config = config
        self._base_url = urljoin(self._config.domain, "v2/public/")

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
    def _user_agent():
        return f"encord-sdk-python/{encord_version} python/{platform.python_version()}"

    def _headers(self):
        return {
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "Content-Type": "application/json",
            HEADER_USER_AGENT: self._user_agent(),
        }

    def get(self, path: str, params: Optional[Dict[str, str]] = None, result_type=None) -> Dict[str, Any]:
        req = requests.Request(
            method="GET",
            url=urljoin(self._base_url, path),
            headers=self._headers(),
            params=params,
        ).prepare()

        req = sign_request(req, self._config.public_key_hex, self._config.private_key)

        timeouts = (self._config.write_timeout, self._config.read_timeout)
        req_settings = self._config.requests_settings
        with create_new_session(
            max_retries=req_settings.max_retries, backoff_factor=req_settings.backoff_factor
        ) as session:
            res = session.send(req, timeout=timeouts)
            context = self._exception_context_from_response(res)

            if res.status_code != 200:
                self._handle_error(res, context)

            try:
                res_json = res.json()
            except Exception as e:
                raise RequestException(f"Error parsing JSON response: {res.text}", context=context) from e

            return res_json

    @staticmethod
    def _handle_error(response: Response, context: RequestContext):
        try:
            description = response.json()
            raise RequestException(message=description["message"], context=context)
        except JSONDecodeError as e:
            raise RequestException(message="Unexpected server response", context=context) from e