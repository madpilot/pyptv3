import pytest
from mock import Mock
from pyptv3 import Search

class TestRuns:
    @pytest.fixture(scope="module")
    def client(self):
        return Mock()

    def test_term(self, client):
        Search(client).term("Tottenham")
        client.get.assert_called_with("/search/Tottenham", [])

    def test_term_with_spaces(self, client):
        Search(client).term("South Morang")
        client.get.assert_called_with("/search/South%20Morang", [])

    def test_term_with_kwargs(self, client):
        Search(client).term("Tottenham", route_types=[0, 1], latitude=-31.000, longitude=148.000, max_distance=500, include_addresses=True, include_outlets=True, match_stop_by_suburb=True, match_route_by_suburb=True)
        client.get.assert_called_with("/search/Tottenham",[("route_types", 0), ("route_types", 1), ("latitude", -31.000), ("longitude", 148.000), ("max_distance", 500), ("include_addresses", "true"), ("include_outlets", "true"), ("match_stop_by_suburb", "true"), ("match_route_by_suburb", "true")])
