import pytest
from mock import Mock
import json
from pyptv3 import SearchResponse, StopsByDistanceResponse, RoutesResponse, OutletsGeolocationResponse, StatusResponse, ONLINE, TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class TestSearchResponse:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
          {
            "stops": [
              {
                "stop_distance": 0,
                "stop_suburb": "West Footscray",
                "stop_name": "Tottenham Station",
                "stop_id": 1196,
                "route_type": 0,
                "stop_latitude": -37.7992554,
                "stop_longitude": 144.862946,
                "stop_sequence": 0
              }
            ],
            "routes": [],
            "outlets": [],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    @pytest.fixture(scope="module")
    def response_with_outlets(self):
        return json.loads("""
          {
            "stops": [
              {
                "stop_distance": 0,
                "stop_suburb": "West Footscray",
                "stop_name": "Tottenham Station",
                "stop_id": 1196,
                "route_type": 0,
                "stop_latitude": -37.7992554,
                "stop_longitude": 144.862946,
                "stop_sequence": 0
              }
            ],
            "routes": [],
            "outlets": [
              {
                "outlet_distance": 0,
                "outlet_slid_spid": "20022",
                "outlet_name": "Corner Ashley Street and Sunshine Road",
                "outlet_business": "Tottenham Station",
                "outlet_latitude": -37.79926,
                "outlet_longitude": 144.862946,
                "outlet_suburb": "West Footscray",
                "outlet_postcode": 3012,
                "outlet_business_hour_mon": null,
                "outlet_business_hour_tue": null,
                "outlet_business_hour_wed": null,
                "outlet_business_hour_thur": null,
                "outlet_business_hour_fri": null,
                "outlet_business_hour_sat": null,
                "outlet_business_hour_sun": null,
                "outlet_notes": null
              }
            ],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    @pytest.fixture(scope="module")
    def response_with_routes(self):
        return json.loads("""
          {
            "stops": [],
            "routes": [
              {
                "route_name": "Dandenong - Endeavour Hills via Thomas Mitchell Drive",
                "route_number": "861",
                "route_type": 2,
                "route_id": 5335,
                "route_gtfs_id": "4-861"
              }
            ],
            "outlets": [],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    def test_stops(self, response):
        subject = SearchResponse(response)
        assert len(subject.stops) == 1
        assert subject.stops.__class__ == StopsByDistanceResponse
        assert subject.stops[0].distance == 0
        assert subject.stops[0].suburb == "West Footscray"
        assert subject.stops[0].name == "Tottenham Station"
        assert subject.stops[0].id == 1196
        assert subject.stops[0].route_type == TRAIN
        assert subject.stops[0].latitude == -37.7992554
        assert subject.stops[0].longitude == 144.862946
        assert subject.stops[0].sequence == 0

    def test_outlets(self, response_with_outlets):
        subject = SearchResponse(response_with_outlets)
        assert len(subject.outlets) == 1
        assert subject.outlets.__class__ == OutletsGeolocationResponse
        assert subject.outlets[0].distance == 0
        assert subject.outlets[0].id == "20022"
        assert subject.outlets[0].name == "Corner Ashley Street and Sunshine Road"
        assert subject.outlets[0].business == "Tottenham Station"
        assert subject.outlets[0].latitude == -37.79926
        assert subject.outlets[0].longitude == 144.862946
        assert subject.outlets[0].suburb == "West Footscray"
        assert subject.outlets[0].postcode == 3012
        assert subject.outlets[0].business_hour_mon == None
        assert subject.outlets[0].business_hour_tue == None
        assert subject.outlets[0].business_hour_wed == None
        assert subject.outlets[0].business_hour_thur == None
        assert subject.outlets[0].business_hour_fri == None
        assert subject.outlets[0].business_hour_sat == None
        assert subject.outlets[0].business_hour_sun == None
        assert subject.outlets[0].notes == None

    def test_routes(self, response_with_routes):
        subject = SearchResponse(response_with_routes)
        assert len(subject.routes) == 1
        assert subject.routes.__class__ == RoutesResponse
        assert subject.routes[0].name == "Dandenong - Endeavour Hills via Thomas Mitchell Drive"
        assert subject.routes[0].number == "861"
        assert subject.routes[0].type == BUS
        assert subject.routes[0].id == 5335
        assert subject.routes[0].gtfs_id == "4-861"

    def test_status(self, response):
        subject = SearchResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE

