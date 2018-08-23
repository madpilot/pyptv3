import pytest
from mock import Mock
from pyptv3 import Patterns, PatternsResponse

class TestPatterns:
    @pytest.fixture(scope="module")
    def client(self):
        client = Mock()
        client.get.return_value = {"disruptions": [], "departures": [], "stops": {}, "routes": {}, "runs": {}, "directions": {}, "status": {"version": "3.0", "health": 1}}
        return client

    def test_all(self, client):
        assert Patterns(client, 1, 0).all().__class__ == PatternsResponse
        client.get.assert_called_with("/pattern/run/1/route_type/0", [])

    def test_all_with_kwargs(self, client):
        assert Patterns(client, 1, 0).all(expand=["stop", "route"], stop_id=10, date_utc="2018-06-28T07:00:00Z").__class__ == PatternsResponse
        client.get.assert_called_with("/pattern/run/1/route_type/0", [("expand", "stop"), ("expand", "route"), ("stop_id", 10), ("date_utc", "2018-06-28T07:00:00Z")])
