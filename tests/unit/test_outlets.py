import pytest
from mock import Mock
from pyptv3 import Outlets

class TestOutlets:
    @pytest.fixture(scope="module")
    def client(self):
        client = Mock()
        client.get.return_value = {"outlets": [], "status": {"version": "3.0", "health": 1}}
        return client

    def test_all(self, client):
        Outlets(client).all()
        client.get.assert_called_with("/outlets", [])

    def test_all_with_kwargs(self, client):
        Outlets(client).all(max_results=10)
        client.get.assert_called_with("/outlets", [("max_results", 10)])

    def test_by_location(self, client):
        Outlets(client).by_location(37.8136, 144.9631)
        client.get.assert_called_with("/outlets/location/37.8136,144.9631", [])

    def test_by_location_with_kwargs(self, client):
        Outlets(client).by_location(37.8136, 144.9631, max_results=10, max_distance=1000)
        client.get.assert_called_with("/outlets/location/37.8136,144.9631", [("max_results", 10), ("max_distance", 1000)])
