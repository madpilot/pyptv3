import pytest
from mock import Mock
import json
import datetime
from pyptv3 import PatternsResponse, DepartureResponse, StopByDistanceResponse, RouteResponse, RunResponse, DirectionResponse, DisruptionResponse, StatusResponse, ONLINE, TRAIN

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
            "disruptions": [],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    @pytest.fixture(scope="module")
    def response_with_stops(self):
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
              }
            ],
            "stops": {
              "1196": {
                "stop_distance": 0,
                "stop_suburb": "West Footscray",
                "stop_name": "Tottenham",
                "stop_id": 1196,
                "route_type": 0,
                "stop_latitude": -37.7992554,
                "stop_longitude": 144.862946,
                "stop_sequence": 0
              }
            },
            "routes": {},
            "runs": {},
            "directions": {},
            "disruptions": [],
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
            "routes": {
              "14": {
                "route_type": 0,
                "route_id": 14,
                "route_name": "Sunbury",
                "route_number": "",
                "route_gtfs_id": "2-SYM"
              }
            },
            "runs": {},
            "directions": {},
            "disruptions": [],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    @pytest.fixture(scope="module")
    def response_with_runs(self):
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
            "runs": {
              "954708": {
                "run_id": 954708,
                "route_id": 14,
                "route_type": 0,
                "final_stop_id": 1071,
                "destination_name": "Flinders Street",
                "status": "scheduled",
                "direction_id": 1,
                "run_sequence": 0,
                "express_stop_count": 1,
                "vehicle_position": null,
                "vehicle_descriptor": null
              }
            },
            "directions": {},
            "disruptions": [],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    @pytest.fixture(scope="module")
    def response_with_directions(self):
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
            "directions": {
              "1": {
                "direction_id": 1,
                "direction_name": "City (Flinders Street)",
                "route_id": 14,
                "route_type": 0
              },
              "13": {
                "direction_id": 13,
                "direction_name": "Sunbury",
                "route_id": 14,
                "route_type": 0
              }
            },
            "disruptions": [],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)


    @pytest.fixture(scope="module")
    def response_with_disruptions(self):
        return json.loads("""
          {
            "departures": [
              {
                  "stop_id": 1008,
                  "route_id": 11,
                  "run_id": 952695,
                  "direction_id": 10,
                  "disruption_ids": [
                    143053
                  ],
                  "scheduled_departure_utc": "2018-08-13T14:21:00Z",
                  "estimated_departure_utc": null,
                  "at_platform": false,
                  "platform_number": "4",
                  "flags": "",
                  "departure_sequence": 0
                },
                {
                  "stop_id": 1008,
                  "route_id": 6,
                  "run_id": 952539,
                  "direction_id": 5,
                  "disruption_ids": [
                    142498
                  ],
                  "scheduled_departure_utc": "2018-08-13T14:26:00Z",
                  "estimated_departure_utc": null,
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
            "disruptions": [
                {
                  "disruption_id": 142498,
                  "title": "Frankston line stations: Temporary car park closures and changes to pedestrian access until late-2018",
                  "url": "http://ptv.vic.gov.au/live-travel-updates/article/frankston-line-stations-temporary-car-park-closures-and-changes-to-pedestrian-access-until-late-2018",
                  "description": "There will be full and partial temporary long-term and short-term closures of station car parks and changes to pedestrian access in and around stations on the Frankston line, due to works as part of the Level Crossing Removal Project.",
                  "disruption_status": "Current",
                  "disruption_type": "Planned Closure",
                  "published_on": "2018-07-10T01:34:18Z",
                  "last_updated": "2018-08-13T06:26:07Z",
                  "from_date": "2018-07-10T01:16:00Z",
                  "to_date": "2018-12-30T16:00:00Z",
                  "routes": [
                    {
                      "route_type": 0,
                      "route_id": 6,
                      "route_name": "Frankston",
                      "route_number": "",
                      "route_gtfs_id": "2-FKN",
                      "direction": null
                    }
                  ]
                }
            ],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)


    def test_departures(self, response):
        subject = PatternsResponse(response)
        assert len(subject.departures) == 2

        assert subject.departures[0].__class__ == DepartureResponse
        departure = subject.departures[0]

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
        subject = PatternsResponse(response)
        assert len(subject.departures) == 2

        assert subject.departures[1].__class__ == DepartureResponse
        departure = subject.departures[1]

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

    def test_departures_with_stops(self, response_with_stops):
        subject = PatternsResponse(response_with_stops)
        assert len(subject.stops.keys()) == 1
        assert subject.stops["1196"].__class__ == StopByDistanceResponse
        stop = subject.stops["1196"]

        assert stop.distance == 0
        assert stop.suburb == "West Footscray"
        assert stop.name == "Tottenham"
        assert stop.id == 1196
        assert stop.route_type == TRAIN
        assert stop.latitude == -37.7992554
        assert stop.longitude == 144.862946
        assert stop.sequence == 0

    def test_departures_with_routes(self, response_with_routes):
        subject = PatternsResponse(response_with_routes)
        assert len(subject.routes.keys()) == 1
        assert subject.routes["14"].__class__ == RouteResponse
        route = subject.routes["14"]

        assert route.type == TRAIN
        assert route.route_id == 14
        assert route.name == "Sunbury"
        assert route.number == ""
        assert route.gtfs_id == "2-SYM"

    def test_departures_with_runs(self, response_with_runs):
        subject = PatternsResponse(response_with_runs)
        assert len(subject.runs.keys()) == 1
        assert subject.runs["954708"].__class__ == RunResponse
        run = subject.runs["954708"]

        assert run.id == 954708
        assert run.route_id == 14
        assert run.route_type == TRAIN
        assert run.final_stop_id == 1071
        assert run.destination_name == "Flinders Street"
        assert run.status == "scheduled"
        assert run.direction_id == 1
        assert run.sequence == 0
        assert run.express_stop_count == 1
        assert run.vehicle_position == None
        assert run.vehicle_descriptor == None

    def test_departures_with_directions(self, response_with_directions):
        subject = PatternsResponse(response_with_directions)
        assert len(subject.directions.keys()) == 2
        assert subject.directions["1"].__class__ == DirectionResponse
        direction = subject.directions["1"]

        assert direction.direction_id == 1
        assert direction.name == "City (Flinders Street)"
        assert direction.route_id == 14
        assert direction.route_type == TRAIN

    def test_departures_with_disruptions(self, response_with_disruptions):
        subject = PatternsResponse(response_with_disruptions)
        assert len(subject.disruptions) == 1
        assert subject.disruptions[0].__class__ == DisruptionResponse
        disruption = subject.disruptions[0]

        assert disruption.disruption_id == 142498
        assert disruption.title == "Frankston line stations: Temporary car park closures and changes to pedestrian access until late-2018"
        assert disruption.url == "http://ptv.vic.gov.au/live-travel-updates/article/frankston-line-stations-temporary-car-park-closures-and-changes-to-pedestrian-access-until-late-2018"
        assert disruption.description == "There will be full and partial temporary long-term and short-term closures of station car parks and changes to pedestrian access in and around stations on the Frankston line, due to works as part of the Level Crossing Removal Project."
        assert disruption.status == "Current"
        assert disruption.type == "Planned Closure"
        assert disruption.published_on == datetime.datetime(2018, 7, 10, 1, 34, 18)
        assert disruption.last_updated == datetime.datetime(2018, 8, 13, 6, 26, 7)
        assert disruption.from_date == datetime.datetime(2018, 7, 10, 1, 16, 0)
        assert disruption.to_date == datetime.datetime(2018, 12, 30, 16, 0, 0)
        assert disruption.routes[0].type == TRAIN
        assert disruption.routes[0].route_id == 6
        assert disruption.routes[0].name == "Frankston"
        assert disruption.routes[0].number == ""
        assert disruption.routes[0].gtfs_id == "2-FKN"
        assert disruption.routes[0].direction == None


    def test_status(self, response):
        subject = PatternsResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE


    def test_repr(self, response):
        subject = PatternsResponse(response)
        assert subject.__repr__().__class__ == str
