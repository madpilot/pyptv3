import pytest
from mock import Mock
from pyptv3 import RouteTypes

class TestRoutes:
    @pytest.fixture(scope="module")
    def client(self):
        return Mock()

    def test_all(self, client):
        RouteTypes(client).all()
        client.get.assert_called_with("/route_types")
