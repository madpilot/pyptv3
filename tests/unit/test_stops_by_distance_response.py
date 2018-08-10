import pytest
from mock import Mock
import json
from pyptv3 import StopsByDistanceResponse, StopByDistanceResponse, StatusResponse, ONLINE, TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class TestStopsByDistanceResponse:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
          {
              "stops": [
                {
                  "stop_distance": 172.131989,
                  "stop_suburb": "Maidstone",
                  "stop_name": "Alma St/Ashley St ",
                  "stop_id": 20905,
                  "route_type": 2,
                  "stop_latitude": -37.79406,
                  "stop_longitude": 144.8631,
                  "stop_sequence": 0
                },
                {
                  "stop_distance": 180.100891,
                  "stop_suburb": "West Footscray",
                  "stop_name": "Brunswick St/Essex St ",
                  "stop_id": 19730,
                  "route_type": 2,
                  "stop_latitude": -37.79234,
                  "stop_longitude": 144.866089,
                  "stop_sequence": 1
                },
                {
                  "stop_distance": 183.405716,
                  "stop_suburb": "West Footscray",
                  "stop_name": "274 Essex St ",
                  "stop_id": 20192,
                  "route_type": 2,
                  "stop_latitude": -37.792244,
                  "stop_longitude": 144.865952,
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
        subject = StopsByDistanceResponse(response)
        assert len(subject.stops) == 3

        assert subject.stops[0].__class__ == StopByDistanceResponse
        assert subject[0].__class__ == StopByDistanceResponse

        assert subject.stops[0].distance == 172.131989
        assert subject.stops[0].suburb == "Maidstone"
        assert subject.stops[0].name == "Alma St/Ashley St"
        assert subject.stops[0].id == 20905
        assert subject.stops[0].route_type == BUS
        assert subject.stops[0].latitude == -37.79406
        assert subject.stops[0].longitude == 144.8631
        assert subject.stops[0].sequence == 0

        assert subject.stops[1].distance == 180.100891
        assert subject.stops[1].suburb == "West Footscray"
        assert subject.stops[1].name == "Brunswick St/Essex St"
        assert subject.stops[1].id == 19730
        assert subject.stops[1].route_type == BUS
        assert subject.stops[1].latitude == -37.79234
        assert subject.stops[1].longitude == 144.866089
        assert subject.stops[1].sequence == 1

        assert subject.stops[2].distance == 183.405716
        assert subject.stops[2].suburb == "West Footscray"
        assert subject.stops[2].name == "274 Essex St"
        assert subject.stops[2].id == 20192
        assert subject.stops[2].route_type == BUS
        assert subject.stops[2].latitude == -37.792244
        assert subject.stops[2].longitude == 144.865952
        assert subject.stops[2].sequence == 2

    def test_status(self, response):
        subject = StopsByDistanceResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE

