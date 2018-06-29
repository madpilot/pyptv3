import pytest
from mock import Mock
from pyptv3 import Routes

class TestRoutes:
    @pytest.fixture(scope="module")
    def client(self):
        return Mock()

    def test_all(self, client):
        Routes(client).all()
        client.get.assert_called_with("/routes", [])

    def test_all_with_kwargs(self, client):
        Routes(client).all(route_name="Sunbury")
        client.get.assert_called_with("/routes", [("route_name", "Sunbury")])

    def test_by_id(self, client):
        Routes(client).by_id(4225)
        client.get.assert_called_with("/routes/4225")
