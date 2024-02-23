from unittest.mock import MagicMock, patch

import pytest
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from requests import Response, Session

from encord.configs import UserConfig
from encord.http.v2.api_client import ApiClient
from encord.orm.analytics import CollaboratorTimer

PRIVATE_KEY = Ed25519PrivateKey.generate()


from encord.exceptions import (
    AuthenticationError,
    AuthorisationError,
    ResourceNotFoundError,
    UnknownException,
)


@pytest.fixture
def api_client():
    return ApiClient(config=UserConfig(PRIVATE_KEY))


@patch.object(Session, "send")
def test_response_mapping_status_codes_to_exception_type_500(send: MagicMock, api_client: ApiClient):
    res = Response()
    res.status_code = 500
    send.return_value = res

    with pytest.raises(UnknownException):
        api_client.get("/", params=None, result_type=CollaboratorTimer)


@patch.object(Session, "send")
def test_response_mapping_status_codes_to_exception_type_401(send: MagicMock, api_client: ApiClient):
    res = Response()
    res.status_code = 401
    send.return_value = res

    with pytest.raises(AuthenticationError):
        api_client.get("/", params=None, result_type=CollaboratorTimer)


@patch.object(Session, "send")
def test_response_mapping_status_codes_to_exception_type_403(send: MagicMock, api_client: ApiClient):
    res = Response()
    res.status_code = 403
    send.return_value = res

    with pytest.raises(AuthorisationError):
        api_client.get("/", params=None, result_type=CollaboratorTimer)


@patch.object(Session, "send")
def test_response_mapping_status_codes_to_exception_type_404(send: MagicMock, api_client: ApiClient):
    res = Response()
    res.status_code = 404
    send.return_value = res

    with pytest.raises(ResourceNotFoundError):
        api_client.get("/", params=None, result_type=CollaboratorTimer)


@patch.object(Session, "send")
def test_response_mapping_status_codes_to_exception_type_unknown(send: MagicMock, api_client: ApiClient):
    res = Response()
    res.status_code = 66
    send.return_value = res

    with pytest.raises(UnknownException):
        api_client.get("/", params=None, result_type=CollaboratorTimer)
