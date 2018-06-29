import pytest
from mock import Mock
from pyptv3 import Disruptions

class TestDisruptions:
    @pytest.fixture(scope="module")
    def client(self):
        return Mock()

    def test_all(self, client):
        Disruptions(client).all()
        client.get.assert_called_with("/disruptions", [])

    def test_all_with_kwargs(self, client):
        Disruptions(client).all(disruption_status="current")
        client.get.assert_called_with("/disruptions", [("disruption_status", "current")])

    def test_by_route(self, client):
        Disruptions(client).by_route(123)
        client.get.assert_called_with("/disruptions/route/123", [])

    def test_by_route_kwargs(self, client):
        Disruptions(client).by_route(123, disruption_status="current")
        client.get.assert_called_with("/disruptions/route/123", [("disruption_status", "current")])

    def test_by_id(self, client):
        Disruptions(client).by_id(1234567)
        client.get.assert_called_with("/disruptions/1234567")
