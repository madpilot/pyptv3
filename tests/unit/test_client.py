import pytest
from urllib.error import HTTPError
from mock import Mock
from pyptv3 import Client, InvalidRequestError, AccessDeniedError, NotFoundError, UnknownError

class TestClient:
    @pytest.fixture(scope="module")
    def client(self):
        return Client("developer_id", "api_key")

    def test_signature(self, client, mocker):
        reader = Mock()
        reader.read.return_value.decode.return_value = '{}'

        urlopen = mocker.patch('urllib.request.urlopen', return_value=reader)
        client.get("/routes")
        urlopen.assert_called_once_with("https://timetableapi.ptv.vic.gov.au/v3/routes?devid=developer_id&signature=98F14D77895AD24EBF2E84BC34386A37C9AA1E81")

    def test_successful_get(self, client, mocker):
        reader = Mock()
        reader.read.return_value.decode.return_value = '{}'

        urlopen = mocker.patch('urllib.request.urlopen', return_value=reader)
        assert client.get("/") == {}

    def test_invalid_request_get(self, client, mocker):
        urlopen = mocker.patch('urllib.request.urlopen', side_effect=HTTPError("/", 400, "Invalid Request", [], None))

        with pytest.raises(InvalidRequestError) as e_info:
            client.get("/")

        assert str(e_info.value) == "Invalid Request"

    def test_access_denied_get(self, client, mocker):
        urlopen = mocker.patch('urllib.request.urlopen', side_effect=HTTPError("/", 403, "Access Denied", [], None))

        with pytest.raises(AccessDeniedError) as e_info:
            client.get("/")

        assert str(e_info.value) == "Access Denied"

    def test_not_found_get(self, client, mocker):
        urlopen = mocker.patch('urllib.request.urlopen', side_effect=HTTPError("/", 404, "Not Found", [], None))

        with pytest.raises(NotFoundError) as e_info:
            client.get("/")

        assert str(e_info.value) == "Not Found"

    def test_unknown_error_get(self, client, mocker):
        urlopen = mocker.patch('urllib.request.urlopen', side_effect=HTTPError("/", 500, "Server Error", [], None))

        with pytest.raises(UnknownError) as e_info:
            client.get("/")

        assert str(e_info.value) == "Code: 500 - Server Error"
