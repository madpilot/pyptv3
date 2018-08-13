import pytest
from mock import Mock
import datetime
import json
from pyptv3 import SingleDisruptionResponse, DisruptionResponse, StatusResponse, ONLINE, TRAIN

class TestDisruptionsResponse:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
            {
              "disruption": {
                "disruption_id": 144252,
                "title": "Seymour line: Coaches replacing selected trains from Sunday 12 August to Wednesday 15 August 2018",
                "url": "http://ptv.vic.gov.au/live-travel-updates/article/seymour-and-shepparton-lines-coaches-replacing-selected-trains-from-sunday-12-august-to-wednesday-15-august-2018",
                "description": "Road coaches replace selected evening trains on the Seymour line from Sunday 12 August to Wednesday 15 August 2018, due to Metro track works.",
                "disruption_status": "Current",
                "disruption_type": "Planned Works",
                "published_on": null,
                "last_updated": null,
                "from_date": null,
                "to_date": null,
                "routes": []
              },
              "status": {
                "version": "3.0",
                "health": 1
              }
            }
        """)


    def test_disruptions(self, response):
        subject = SingleDisruptionResponse(response)

        assert subject.disruption.__class__ == DisruptionResponse
        assert subject.disruption.id == 144252
        assert subject.disruption.title == "Seymour line: Coaches replacing selected trains from Sunday 12 August to Wednesday 15 August 2018"
        assert subject.disruption.url == "http://ptv.vic.gov.au/live-travel-updates/article/seymour-and-shepparton-lines-coaches-replacing-selected-trains-from-sunday-12-august-to-wednesday-15-august-2018"
        assert subject.disruption.description == "Road coaches replace selected evening trains on the Seymour line from Sunday 12 August to Wednesday 15 August 2018, due to Metro track works."
        assert subject.disruption.status == "Current"
        assert subject.disruption.type == "Planned Works"
        assert subject.disruption.published_on == None
        assert subject.disruption.last_updated == None
        assert subject.disruption.from_date == None
        assert subject.disruption.to_date == None
        assert subject.disruption.routes == []


    def test_status(self, response):
        subject = SingleDisruptionResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE

