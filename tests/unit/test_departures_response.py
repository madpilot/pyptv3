import pytest
from mock import Mock
import json
import datetime
from pyptv3 import DeparturesResponse, DepartureResponse, StatusResponse, ONLINE

class TestDeparturesResponse:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
          {
            "departures": [
              {
                "stop_id": 1196,
                "route_id": 14,
                "run_id": 954661,
                "direction_id": 13,
                "disruption_ids": [],
                "scheduled_departure_utc": "2018-08-13T14:17:00Z",
                "estimated_departure_utc": null,
                "at_platform": false,
                "platform_number": "2",
                "flags": "",
                "departure_sequence": 0
              },
              {
                "stop_id": 1196,
                "route_id": 14,
                "run_id": 954661,
                "direction_id": 13,
                "disruption_ids": [],
                "scheduled_departure_utc": "2018-08-14T14:17:00Z",
                "estimated_departure_utc": "2018-08-14T15:17:00Z",
                "at_platform": false,
                "platform_number": "2",
                "flags": "",
                "departure_sequence": 0
              }
            ],
            "stops": {},
            "routes": {},
            "runs": {},
            "directions": {},
            "disruptions": {},
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    def test_departures(self, response):
        subject = DeparturesResponse(response)
        assert len(subject.departures) == 2

        assert subject.departures[0].__class__ == DepartureResponse
        assert subject[0].__class__ == DepartureResponse
        departure = subject[0]

        assert departure.stop_id == 1196
        assert departure.route_id == 14
        assert departure.run_id == 954661
        assert departure.direction_id == 13
        assert departure.disruption_ids == []
        assert departure.scheduled_departure == datetime.datetime(2018, 8, 13, 14, 17, 00)
        assert departure.estimated_departure == None
        assert departure.at_platform == False
        assert departure.platform_number == "2"
        assert departure.flags == ""
        assert departure.sequence == 0

    def test_departures_with_estimated_departure(self, response):
        subject = DeparturesResponse(response)
        assert len(subject.departures) == 2

        assert subject.departures[1].__class__ == DepartureResponse
        assert subject[1].__class__ == DepartureResponse
        departure = subject[1]

        assert departure.stop_id == 1196
        assert departure.route_id == 14
        assert departure.run_id == 954661
        assert departure.direction_id == 13
        assert departure.disruption_ids == []
        assert departure.scheduled_departure == datetime.datetime(2018, 8, 14, 14, 17, 00)
        assert departure.estimated_departure == datetime.datetime(2018, 8, 14, 15, 17, 00)
        assert departure.at_platform == False
        assert departure.platform_number == "2"
        assert departure.flags == ""
        assert departure.sequence == 0

    def test_status(self, response):
        subject = DeparturesResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE

