import pytest
from mock import Mock
from pyptv3 import Stops

class TestStops:
    @pytest.fixture(scope="module")
    def client(self):
        return Mock()

    def test_by_stop(self, client):
        Stops(client).by_stop(1, 0)
        client.get.assert_called_with("/stops/1/route_type/0", [])

    def test_by_stop_with_kwargs(self, client):
        Stops(client).by_stop(1, 0, stop_location=True, stop_amenities=True, stop_accessibility=True, stop_contact=True, stop_ticket=True, gtfs=True)
        client.get.assert_called_with("/stops/1/route_type/0", [("stop_location", "true"), ("stop_amenities", "true"), ("stop_accessibility", "true"), ("stop_contact", "true"), ("stop_ticket", "true"), ("gtfs", "true")])

    def test_by_route(self, client):
        Stops(client).by_route(10, 0)
        client.get.assert_called_with("/stops/route/10/route_type/0", [])

    def test_by_route_with_kwargs(self, client):
        Stops(client).by_route(10, 0, stop_location=True, stop_amenities=True, stop_accessibility=True, stop_contact=True, stop_ticket=True, gtfs=True)
        client.get.assert_called_with("/stops/route/10/route_type/0", [("stop_location", "true"), ("stop_amenities", "true"), ("stop_accessibility", "true"), ("stop_contact", "true"), ("stop_ticket", "true"), ("gtfs", "true")])

    def test_by_location(self, client):
        Stops(client).by_location(-38.0, 142.0)
        client.get.assert_called_with("/stops/location/-38.0,142.0", [])

    def test_by_location_with_kwargs(self, client):
        Stops(client).by_location(-38.0, 142.0, stop_location=True, stop_amenities=True, stop_accessibility=True, stop_contact=True, stop_ticket=True, gtfs=True)
        client.get.assert_called_with("/stops/location/-38.0,142.0", [("stop_location", "true"), ("stop_amenities", "true"), ("stop_accessibility", "true"), ("stop_contact", "true"), ("stop_ticket", "true"), ("gtfs", "true")])
