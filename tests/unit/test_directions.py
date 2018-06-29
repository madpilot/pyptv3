import pytest
from mock import Mock
from pyptv3 import Directions

class TestDirections:
    @pytest.fixture(scope="module")
    def client(self):
        return Mock()

    def test_by_id(self, client):
        Directions(client).by_id(1341)
        client.get.assert_called_with("/directions/1341")

    def test_by_route(self, client):
        Directions(client).by_route(221)
        client.get.assert_called_with("/directions/route/221")

    def test_by_route_type(self, client):
        Directions(client).by_route_type(1341, 0)
        client.get.assert_called_with("/directions/1341/route_type/0")
