import pytest
from mock import Mock
import json
from pyptv3 import StopOnRoutesResponse, StopOnRouteResponse, StatusResponse, ONLINE, TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class TestStopOnRoutesResponse:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
          {
              "stops": [
                {
                  "stop_suburb": "Baxter",
                  "stop_name": "Baxter Station",
                  "stop_id": 1015,
                  "route_type": 0,
                  "stop_latitude": -38.194046,
                  "stop_longitude": 145.160522,
                  "stop_sequence": 0
                },
                {
                  "stop_suburb": "Bittern",
                  "stop_name": "Bittern Station",
                  "stop_id": 1022,
                  "route_type": 0,
                  "stop_latitude": -38.33739,
                  "stop_longitude": 145.178024,
                  "stop_sequence": 1
                },
                {
                  "stop_suburb": "Crib Point",
                  "stop_name": "Crib Point Station",
                  "stop_id": 1046,
                  "route_type": 0,
                  "stop_latitude": -38.36612,
                  "stop_longitude": 145.204041,
                  "stop_sequence": 2
                }
              ],
              "status": {
                "version": "3.0",
                "health": 1
              }
            }
        """)

    def test_stops(self, response):
        subject = StopOnRoutesResponse(response)
        assert len(subject.stops) == 3

        assert subject.stops[0].__class__ == StopOnRouteResponse
        assert subject[0].__class__ == StopOnRouteResponse

        assert subject.stops[0].suburb == "Baxter"
        assert subject.stops[0].name == "Baxter Station"
        assert subject.stops[0].id == 1015
        assert subject.stops[0].route_type == TRAIN
        assert subject.stops[0].latitude == -38.194046
        assert subject.stops[0].longitude == 145.160522
        assert subject.stops[0].sequence == 0

        assert subject.stops[1].suburb == "Bittern"
        assert subject.stops[1].name == "Bittern Station"
        assert subject.stops[1].id == 1022
        assert subject.stops[1].route_type == TRAIN
        assert subject.stops[1].latitude == -38.33739
        assert subject.stops[1].longitude == 145.178024
        assert subject.stops[1].sequence == 1

        assert subject.stops[2].suburb == "Crib Point"
        assert subject.stops[2].name == "Crib Point Station"
        assert subject.stops[2].id == 1046
        assert subject.stops[2].route_type == TRAIN
        assert subject.stops[2].latitude == -38.36612
        assert subject.stops[2].longitude == 145.204041
        assert subject.stops[2].sequence == 2

    def test_status(self, response):
        subject = StopOnRoutesResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE

