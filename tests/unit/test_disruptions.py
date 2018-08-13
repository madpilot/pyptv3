import pytest
from mock import Mock
from pyptv3 import Disruptions, DisruptionsResponse, SingleDisruptionResponse

class TestDisruptions:
    @pytest.fixture(scope="module")
    def client(self):
        client = Mock()
        client.get.return_value = {"disruptions": {"general": [], "metro_train": None, "metro_tram": None, "metro_bus": None, "regional_train": None, "regional_coach": None, "regional_bus": None}, "status": {"version": "3.0", "health": 1}}
        return client

    @pytest.fixture(scope="module")
    def single_client(self):
        client = Mock()
        client.get.return_value = {"disruption": {
            "disruption_id": 144252,
            "title": "Seymour line: Coaches replacing selected trains from Sunday 12 August to Wednesday 15 August 2018",
            "url": "http://ptv.vic.gov.au/live-travel-updates/article/seymour-and-shepparton-lines-coaches-replacing-selected-trains-from-sunday-12-august-to-wednesday-15-august-2018",
            "description": "Road coaches replace selected evening trains on the Seymour line from Sunday 12 August to Wednesday 15 August 2018, due to Metro track works.",
            "disruption_status": "Current",
            "disruption_type": "Planned Works",
            "published_on": None,
            "last_updated": None,
            "from_date": None,
            "to_date": None,
            "routes": []
        }, "status": {"version": "3.0", "health": 1}}
        return client

    def test_all(self, client):
        assert Disruptions(client).all().__class__ == DisruptionsResponse
        client.get.assert_called_with("/disruptions", [])

    def test_all_with_kwargs(self, client):
        assert Disruptions(client).all(disruption_status="current").__class__ == DisruptionsResponse
        client.get.assert_called_with("/disruptions", [("disruption_status", "current")])

    def test_by_route(self, client):
        assert Disruptions(client).by_route(123).__class__ == DisruptionsResponse
        client.get.assert_called_with("/disruptions/route/123", [])

    def test_by_route_kwargs(self, client):
        assert Disruptions(client).by_route(123, disruption_status="current").__class__ == DisruptionsResponse
        client.get.assert_called_with("/disruptions/route/123", [("disruption_status", "current")])

    def test_by_id(self, single_client):
        assert Disruptions(single_client).by_id(1234567).__class__ == SingleDisruptionResponse
        single_client.get.assert_called_with("/disruptions/1234567")
