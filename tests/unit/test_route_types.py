import pytest
from mock import Mock
from pyptv3 import RouteTypes

class TestRoutes:
    @pytest.fixture(scope="module")
    def client(self):
        client = Mock()
        client.get.return_value = {"route_types": [], "status": {"version": "3.0", "health": 1}}
        return client

    def test_all(self, client):
        RouteTypes(client).all()
        client.get.assert_called_with("/route_types")
