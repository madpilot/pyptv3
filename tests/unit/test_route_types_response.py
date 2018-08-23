import pytest
from mock import Mock
import json
from pyptv3 import RouteTypesResponse, RouteTypeResponse, StatusResponse, ONLINE, TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class TestRoutesTypesResponse:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
          {
            "route_types": [
              {
                "route_type_name": "Train",
                "route_type": 0
              },
              {
                "route_type_name": "Tram",
                "route_type": 1
              },
              {
                "route_type_name": "Bus",
                "route_type": 2
              },
              {
                "route_type_name": "Vline",
                "route_type": 3
              },
              {
                "route_type_name": "Night Bus",
                "route_type": 4
              }
            ],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    def test_types(self, response):
        subject = RouteTypesResponse(response)
        assert len(subject.types) == 5

        assert subject.types[0].__class__ == RouteTypeResponse
        assert subject[0].__class__ == RouteTypeResponse

        assert subject.types[0].name == "Train"
        assert subject.types[0].type == TRAIN

        assert subject.types[1].name == "Tram"
        assert subject.types[1].type == TRAM

        assert subject.types[2].name == "Bus"
        assert subject.types[2].type == BUS

        assert subject.types[3].name == "Vline"
        assert subject.types[3].type == VLINE_TRAIN

        assert subject.types[4].name == "Night Bus"
        assert subject.types[4].type == NIGHT_BUS

    def test_status(self, response):
        subject = RouteTypesResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE

    def test_repr(self, response):
        subject = RouteTypesResponse(response)
        assert subject.__repr__().__class__ == str
