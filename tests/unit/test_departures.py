import pytest
from mock import Mock
from pyptv3 import Departures, DeparturesResponse

class TestDepartures:
    @pytest.fixture(scope="module")
    def client(self):
        client = Mock()
        client.get.return_value = {"departures": [], "stops": {}, "routes": {}, "runs": {}, "directions": {}, "disruptions": {}, "status": {"version": "3.0", "health": 1}}
        return client

    def test_all(self, client):
        assert Departures(client, 0, 1341).all().__class__ == DeparturesResponse
        client.get.assert_called_with("/departures/route_type/0/stop/1341", [])

    def test_all_with_kwargs(self, client):
        Departures(client, 0, 1341).all(platform_numbers=[0, 1], direction_id=1, look_backwards=False, gtfs=123, date_utc="2018-06-28T07:00:00Z", max_results=10, include_cancelled=True, expand=["stop", "route"]).__class__ == DeparturesResponse
        client.get.assert_called_with("/departures/route_type/0/stop/1341", [("platform_numbers", 0), ("platform_numbers", 1), ("direction_id", 1), ("look_backwards", "false"), ("gtfs", 123), ("date_utc", "2018-06-28T07:00:00Z"), ("max_results", 10), ("include_cancelled", "true"), ("expand", "stop"), ("expand", "route")])

    def test_by_route(self, client):
        assert Departures(client, 0, 1341).by_route(4122).__class__ == DeparturesResponse
        client.get.assert_called_with("/departures/route_type/0/stop/1341/route/4122", [])

    def test_by_route_with_kwargs(self, client):
        assert Departures(client, 0, 1341).by_route(4122, platform_numbers=[0, 1], direction_id=1, look_backwards=False, gtfs=123, date_utc="2018-06-28T07:00:00Z", max_results=10, include_cancelled=True, expand=["stop", "route"]).__class__ == DeparturesResponse
        client.get.assert_called_with("/departures/route_type/0/stop/1341/route/4122", [("platform_numbers", 0), ("platform_numbers", 1), ("direction_id", 1), ("look_backwards", "false"), ("gtfs", 123), ("date_utc", "2018-06-28T07:00:00Z"), ("max_results", 10), ("include_cancelled", "true"), ("expand", "stop"), ("expand", "route")])
