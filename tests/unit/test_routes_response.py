import pytest
from mock import Mock
import json
from pyptv3 import RoutesResponse, RouteResponse, StatusResponse, ONLINE, TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class TestRoutesResponse:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
          {
            "routes": [
              {
                "route_type": 1,
                "route_id": 721,
                "route_name": "East Coburg - South Melbourne Beach",
                "route_number": "1",
                "route_gtfs_id": "3-001"
              },
              {
                "route_type": 1,
                "route_id": 722,
                "route_name": "Box Hill - Port Melbourne",
                "route_number": "109",
                "route_gtfs_id": "3-109"
              },
              {
                "route_type": 1,
                "route_id": 724,
                "route_name": "Melbourne University - Kew via St Kilda Beach",
                "route_number": "16",
                "route_gtfs_id": "3-016"
              },
              {
                "route_type": 1,
                "route_id": 725,
                "route_name": "North Coburg - Flinders Street Station & City",
                "route_number": "19",
                "route_gtfs_id": "3-019"
              }
            ],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    def test_routes(self, response):
        subject = RoutesResponse(response)
        assert len(subject.routes) == 4

        assert subject.routes[0].__class__ == RouteResponse
        assert subject[0].__class__ == RouteResponse

        assert subject.routes[0].name == "East Coburg - South Melbourne Beach"
        assert subject.routes[0].type == TRAM
        assert subject.routes[0].number == "1"
        assert subject.routes[0].gtfs_id == "3-001"

        assert subject.routes[1].name == "Box Hill - Port Melbourne"
        assert subject.routes[1].type == TRAM
        assert subject.routes[1].number == "109"
        assert subject.routes[1].gtfs_id == "3-109"

        assert subject.routes[2].name == "Melbourne University - Kew via St Kilda Beach"
        assert subject.routes[2].type == TRAM
        assert subject.routes[2].number == "16"
        assert subject.routes[2].gtfs_id == "3-016"

        assert subject.routes[3].name == "North Coburg - Flinders Street Station & City"
        assert subject.routes[3].type == TRAM
        assert subject.routes[3].number == "19"
        assert subject.routes[3].gtfs_id == "3-019"

    def test_status(self, response):
        subject = RoutesResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE

