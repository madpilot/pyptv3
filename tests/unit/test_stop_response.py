import pytest
from mock import Mock
import json
from pyptv3 import StopResponse, StatusResponse, ONLINE, TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class TestStopsResponse:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
          {
            "stop": {
              "station_type": "Premium Station",
              "station_description": "The customer service centre is staffed from first to last train, 7 days a week. Protective Services Officers are generally present from 6pm to last train Sunday to Thursday and overnight on Fridays and Saturdays.",
              "route_type": 0,
              "stop_location": null,
              "stop_amenities": null,
              "stop_accessibility": null,
              "stop_id": 1071,
              "stop_name": "Flinders Street"
            },
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    @pytest.fixture(scope="module")
    def response_with_location(self):
        return json.loads("""
          {
              "stop": {
                "station_type": "Premium Station",
                "station_description": "The customer service centre is staffed from first to last train, 7 days a week. Protective Services Officers are generally present from 6pm to last train Sunday to Thursday and overnight on Fridays and Saturdays.",
                "route_type": 0,
                "stop_location": {
                  "gps": {
                    "latitude": -37.81831,
                    "longitude": 144.966965
                  }
                },
                "stop_amenities": null,
                "stop_accessibility": null,
                "stop_id": 1071,
                "stop_name": "Flinders Street "
              },
              "status": {
                "version": "3.0",
                "health": 1
              }
            }
        """)

    @pytest.fixture(scope="module")
    def response_with_amenities(self):
        return json.loads("""
          {
              "stop": {
                "station_type": "Premium Station",
                "station_description": "The customer service centre is staffed from first to last train, 7 days a week. Protective Services Officers are generally present from 6pm to last train Sunday to Thursday and overnight on Fridays and Saturdays.",
                "route_type": 0,
                "stop_location": null,
                "stop_amenities": {
                  "toilet": true,
                  "taxi_rank": true,
                  "car_parking": "0",
                  "cctv": true
                },
                "stop_accessibility": null,
                "stop_id": 1071,
                "stop_name": "Flinders Street "
              },
              "status": {
                "version": "3.0",
                "health": 1
              }
            }
        """)

    @pytest.fixture(scope="module")
    def response_with_accessibility(self):
        return json.loads("""
          {
              "stop": {
                "station_type": "Premium Station",
                "station_description": "The customer service centre is staffed from first to last train, 7 days a week. Protective Services Officers are generally present from 6pm to last train Sunday to Thursday and overnight on Fridays and Saturdays.",
                "route_type": 0,
                "stop_location": null,
                "stop_amenities": null,
                "stop_accessibility": {
                  "lighting": true,
                  "stairs": true,
                  "escalator": true,
                  "lifts": true,
                  "hearing_loop": false,
                  "tactile_tiles": true,
                  "wheelchair": {
                    "accessible_ramp": false,
                    "accessible_parking": false,
                    "accessible_phone": true,
                    "accessible_toilet": true
                  }
                },
                "stop_id": 1071,
                "stop_name": "Flinders Street "
              },
              "status": {
                "version": "3.0",
                "health": 1
              }
            }
        """)

    def test_stops(self, response):
        subject = StopResponse(response)
        assert subject.details.type == "Premium Station"
        assert subject.details.description == "The customer service centre is staffed from first to last train, 7 days a week. Protective Services Officers are generally present from 6pm to last train Sunday to Thursday and overnight on Fridays and Saturdays."
        assert subject.details.route_type == TRAIN
        assert subject.details.location == None
        assert subject.details.amenities == None
        assert subject.details.accessibility == None
        assert subject.details.id == 1071
        assert subject.details.name == "Flinders Street"

    def test_stops_with_location(self, response_with_location):
        subject = StopResponse(response_with_location)
        assert subject.details.location.gps.latitude == -37.81831
        assert subject.details.location.gps.longitude == 144.966965

    def test_stops_with_amenities(self, response_with_amenities):
        subject = StopResponse(response_with_amenities)
        assert subject.details.amenities.toilet == True
        assert subject.details.amenities.taxi_rank == True
        assert subject.details.amenities.car_parking == "0"
        assert subject.details.amenities.cctv == True

    def test_stops_with_accessibility(self, response_with_accessibility):
        subject = StopResponse(response_with_accessibility)
        assert subject.details.accessibility.lighting == True
        assert subject.details.accessibility.stairs == True
        assert subject.details.accessibility.escalator == True
        assert subject.details.accessibility.lifts == True
        assert subject.details.accessibility.hearing_loop == False
        assert subject.details.accessibility.tactile_tiles == True
        assert subject.details.accessibility.wheelchair.accessible_ramp == False
        assert subject.details.accessibility.wheelchair.accessible_parking == False
        assert subject.details.accessibility.wheelchair.accessible_phone == True
        assert subject.details.accessibility.wheelchair.accessible_toilet == True

    def test_status(self, response):
        subject = StopResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE

