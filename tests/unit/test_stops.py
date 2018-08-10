import pytest
from mock import Mock
from pyptv3 import Stops, StopResponse, StopOnRoutesResponse, StopsByDistanceResponse

class TestStops:
    @pytest.fixture(scope="module")
    def stop_client(self):
        client = Mock()
        client.get.return_value = {
            "stop": {
                "station_type": "Premium Station",
                "station_description": "The customer service centre is staffed from first to last train, 7 days a week. Protective Services Officers are generally present from 6pm to last train Sunday to Thursday and overnight on Fridays and Saturdays.",
                "route_type": 0,
                "stop_location": None,
                "stop_amenities": None,
                "stop_accessibility": None,
                "stop_id": 1071,
                "stop_name": "Flinders Street "},
            "status": {
                "version": "3.0", "health": 1
            }
        }
        return client

    @pytest.fixture(scope="module")
    def client(self):
        client = Mock()
        client.get.return_value = {"stops": [], "status": {"version": "3.0", "health": 1}}
        return client

    def test_by_stop(self, stop_client):
        assert Stops(stop_client).by_stop(1, 0)
        stop_client.get.assert_called_with("/stops/1/route_type/0", []).__class__ == StopResponse

    def test_by_stop_with_kwargs(self, stop_client):
        assert Stops(stop_client).by_stop(1, 0, stop_location=True, stop_amenities=True, stop_accessibility=True, stop_contact=True, stop_ticket=True, gtfs=True).__class__ == StopResponse
        stop_client.get.assert_called_with("/stops/1/route_type/0", [("stop_location", "true"), ("stop_amenities", "true"), ("stop_accessibility", "true"), ("stop_contact", "true"), ("stop_ticket", "true"), ("gtfs", "true")])

    def test_by_route(self, client):
        assert Stops(client).by_route(10, 0).__class__ == StopOnRoutesResponse
        client.get.assert_called_with("/stops/route/10/route_type/0", [])

    def test_by_route_with_kwargs(self, client):
        assert Stops(client).by_route(10, 0, stop_location=True, stop_amenities=True, stop_accessibility=True, stop_contact=True, stop_ticket=True, gtfs=True).__class__ == StopOnRoutesResponse
        client.get.assert_called_with("/stops/route/10/route_type/0", [("stop_location", "true"), ("stop_amenities", "true"), ("stop_accessibility", "true"), ("stop_contact", "true"), ("stop_ticket", "true"), ("gtfs", "true")])

    def test_by_location(self, client):
        assert Stops(client).by_location(-38.0, 142.0).__class__ == StopsByDistanceResponse
        client.get.assert_called_with("/stops/location/-38.0,142.0", [])

    def test_by_location_with_kwargs(self, client):
        assert Stops(client).by_location(-38.0, 142.0, stop_location=True, stop_amenities=True, stop_accessibility=True, stop_contact=True, stop_ticket=True, gtfs=True).__class__ == StopsByDistanceResponse
        client.get.assert_called_with("/stops/location/-38.0,142.0", [("stop_location", "true"), ("stop_amenities", "true"), ("stop_accessibility", "true"), ("stop_contact", "true"), ("stop_ticket", "true"), ("gtfs", "true")])
