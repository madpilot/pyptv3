import pytest
from mock import Mock
import json
from pyptv3 import DirectionsResponse, DirectionResponse, StatusResponse, ONLINE, TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class TestDirectionsResponse:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
          {
              "directions": [
                    {
                          "direction_id": 13,
                          "direction_name": "Sunbury",
                          "route_id": 14,
                          "route_type": 0
                    },
                    {
                          "direction_id": 13,
                          "direction_name": "Flinders Street Station (City)",
                          "route_id": 725,
                          "route_type": 1
                    },
                    {
                          "direction_id": 13,
                          "direction_name": "Brighton Beach",
                          "route_id": 11694,
                          "route_type": 2
                    },
                    {
                          "direction_id": 13,
                          "direction_name": "Barham",
                          "route_id": 1744,
                          "route_type": 3
                    },
                    {
                          "direction_id": 13,
                          "direction_name": "Lilydale",
                          "route_id": 8964,
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
        subject = DirectionsResponse(response)
        assert len(subject.directions) == 5

        assert subject.directions[0].__class__ == DirectionResponse
        assert subject[0].__class__ == DirectionResponse

        assert subject.directions[0].id == 13
        assert subject.directions[0].name == "Sunbury"
        assert subject.directions[0].route_type == TRAIN
        assert subject.directions[0].route_id == 14

        assert subject.directions[1].id == 13
        assert subject.directions[1].name == "Flinders Street Station (City)"
        assert subject.directions[1].route_type == TRAM
        assert subject.directions[1].route_id == 725

        assert subject.directions[2].id == 13
        assert subject.directions[2].name == "Brighton Beach"
        assert subject.directions[2].route_type == BUS
        assert subject.directions[2].route_id == 11694

        assert subject.directions[3].id == 13
        assert subject.directions[3].name == "Barham"
        assert subject.directions[3].route_type == VLINE_TRAIN
        assert subject.directions[3].route_id == 1744

        assert subject.directions[4].id == 13
        assert subject.directions[4].name == "Lilydale"
        assert subject.directions[4].route_type == NIGHT_BUS
        assert subject.directions[4].route_id == 8964

    def test_status(self, response):
        subject = DirectionsResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE


    def test_repr(self, response):
        subject = DirectionsResponse(response)
        assert subject.__repr__().__class__ == str
