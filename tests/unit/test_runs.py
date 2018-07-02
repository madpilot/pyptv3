import pytest
from mock import Mock
from pyptv3 import Runs

class TestRuns:
    @pytest.fixture(scope="module")
    def client(self):
        return Mock()

    def test_by_id(self, client):
        Runs(client).by_id(10)
        client.get.assert_called_with("/runs/10")

    def test_by_id_and_route_type(self, client):
        Runs(client).by_id(10, 0)
        client.get.assert_called_with("/runs/10/route_type/0")

    def test_by_route(self, client):
        Runs(client).by_route(20)
        client.get.assert_called_with("/runs/route/20")

    def test_by_route_and_route_type(self, client):
        Runs(client).by_route(20, 0)
        client.get.assert_called_with("/runs/route/20/route_type/0")
