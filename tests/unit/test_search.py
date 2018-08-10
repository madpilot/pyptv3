import pytest
from mock import Mock
from pyptv3 import Search, SearchResponse

class TestRuns:
    @pytest.fixture(scope="module")
    def client(self):
        client = Mock()
        client.get.return_value = {"stops": [], "routes": [], "outlets": [], "status": {"version": "3.0", "health": 1}}
        return client

    def test_term(self, client):
        assert Search(client).term("Tottenham").__class__ == SearchResponse
        client.get.assert_called_with("/search/Tottenham", [])

    def test_term_with_spaces(self, client):
        assert Search(client).term("South Morang").__class__ == SearchResponse
        client.get.assert_called_with("/search/South%20Morang", [])

    def test_term_with_kwargs(self, client):
        assert Search(client).term("Tottenham", route_types=[0, 1], latitude=-31.000, longitude=148.000, max_distance=500, include_addresses=True, include_outlets=True, match_stop_by_suburb=True, match_route_by_suburb=True).__class__ == SearchResponse
        client.get.assert_called_with("/search/Tottenham",[("route_types", 0), ("route_types", 1), ("latitude", -31.000), ("longitude", 148.000), ("max_distance", 500), ("include_addresses", "true"), ("include_outlets", "true"), ("match_stop_by_suburb", "true"), ("match_route_by_suburb", "true")])
