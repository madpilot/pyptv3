import pytest
from mock import Mock
from pyptv3 import Directions, DirectionsResponse

class TestDirections:
    @pytest.fixture(scope="module")
    def client(self):
        client = Mock()
        client.get.return_value = {"directions": [], "status": {"version": "3.0", "health": 1}}
        return client

    def test_by_id(self, client):
        assert Directions(client).by_id(1341).__class__ == DirectionsResponse
        client.get.assert_called_with("/directions/1341")

    def test_by_route(self, client):
        assert Directions(client).by_route(221).__class__ == DirectionsResponse
        client.get.assert_called_with("/directions/route/221")

    def test_by_route_type(self, client):
        assert Directions(client).by_route_type(1341, 0).__class__ == DirectionsResponse
        client.get.assert_called_with("/directions/1341/route_type/0")
