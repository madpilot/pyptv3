import pytest
from mock import Mock
import datetime
import json
from pyptv3 import DisruptionsResponse, DisruptionResponse, StatusResponse, ONLINE, TRAIN

class TestDisruptionsResponse:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
            {
                "disruptions": {
                    "general": [],
                    "metro_train": [],
                    "metro_tram": [],
                    "metro_bus": [],
                    "regional_train": [],
                    "regional_coach": [],
                    "regional_bus": []
                },
                "status": {
                    "version": "3.0",
                    "health": 1
                }
          }
        """)

    @pytest.fixture(scope="module")
    def null_response(self):
        return json.loads("""
            {
                "disruptions": {
                    "general": [],
                    "metro_train": null,
                    "metro_tram": null,
                    "metro_bus": null,
                    "regional_train": null,
                    "regional_coach": null,
                    "regional_bus": null
                },
                "status": {
                    "version": "3.0",
                    "health": 1
                }
          }
        """)

    @pytest.fixture(scope="module")
    def response_metro_train(self):
        return json.loads("""
            {
                "disruptions": {
                    "general": [],
                    "metro_train": [
                        {
                            "disruption_id": 145833,
                            "title": "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am.",
                            "url": "http://ptv.vic.gov.au/live-travel-updates/",
                            "description": "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am.",
                            "disruption_status": "Current",
                            "disruption_type": "Minor Delays",
                            "published_on": null,
                            "last_updated": null,
                            "from_date": null,
                            "to_date": null,
                            "routes": []
                        }
                    ],
                    "metro_tram": [],
                    "metro_bus": [],
                    "regional_train": [],
                    "regional_coach": [],
                    "regional_bus": []
                },
                "status": {
                    "version": "3.0",
                    "health": 1
                }
          }
        """)

    @pytest.fixture(scope="module")
    def response_metro_train_with_dates(self):
        return json.loads("""
            {
                "disruptions": {
                    "general": [],
                    "metro_train": [
                        {
                            "disruption_id": 145833,
                            "title": "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am.",
                            "url": "http://ptv.vic.gov.au/live-travel-updates/",
                            "description": "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am.",
                            "disruption_status": "Current",
                            "disruption_type": "Minor Delays",
                            "published_on": "2018-08-12T22:57:10Z",
                            "last_updated": "2018-08-12T22:58:59Z",
                            "from_date": "2018-08-12T22:56:00Z",
                            "to_date": "2018-08-14T22:56:00Z",
                            "routes": []
                        }
                    ],
                    "metro_tram": [],
                    "metro_bus": [],
                    "regional_train": [],
                    "regional_coach": [],
                    "regional_bus": []
                },
                "status": {
                    "version": "3.0",
                    "health": 1
                }
          }
        """)

    @pytest.fixture(scope="module")
    def response_metro_train_with_routes(self):
        return json.loads("""
            {
                "disruptions": {
                    "general": [],
                    "metro_train": [
                        {
                            "disruption_id": 145833,
                            "title": "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am.",
                            "url": "http://ptv.vic.gov.au/live-travel-updates/",
                            "description": "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am.",
                            "disruption_status": "Current",
                            "disruption_type": "Minor Delays",
                            "published_on": null,
                            "last_updated": null,
                            "from_date": null,
                            "to_date": null,
                            "routes": [{
                                "route_type": 0,
                                "route_id": 2,
                                "route_name": "Belgrave",
                                "route_number": "",
                                "route_gtfs_id": "2-BEL",
                                "direction": {
                                    "route_direction_id": 20,
                                    "direction_id": 1,
                                    "direction_name": "City (Flinders Street)",
                                    "service_time": null
                                }
                            }]
                        }
                    ],
                    "metro_tram": [],
                    "metro_bus": [],
                    "regional_train": [],
                    "regional_coach": [],
                    "regional_bus": []
                },
                "status": {
                    "version": "3.0",
                    "health": 1
                }
          }
        """)

    @pytest.fixture(scope="module")
    def response_metro_train_with_service_time(self):
        return json.loads("""
            {
                "disruptions": {
                    "general": [],
                    "metro_train": [
                        {
                            "disruption_id": 145833,
                            "title": "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am.",
                            "url": "http://ptv.vic.gov.au/live-travel-updates/",
                            "description": "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am.",
                            "disruption_status": "Current",
                            "disruption_type": "Minor Delays",
                            "published_on": null,
                            "last_updated": null,
                            "from_date": null,
                            "to_date": null,
                            "routes": [{
                                "route_type": 0,
                                "route_id": 2,
                                "route_name": "Belgrave",
                                "route_number": "",
                                "route_gtfs_id": "2-BEL",
                                "direction": {
                                    "route_direction_id": 20,
                                    "direction_id": 1,
                                    "direction_name": "City (Flinders Street)",
                                    "service_time": "12:45:00"
                                }
                            }]
                        }
                    ],
                    "metro_tram": [],
                    "metro_bus": [],
                    "regional_train": [],
                    "regional_coach": [],
                    "regional_bus": []
                },
                "status": {
                    "version": "3.0",
                    "health": 1
                }
          }
        """)

    @pytest.fixture(scope="module")
    def response_metro_tram(self):
        return json.loads("""
            {
                "disruptions": {
                    "general": [],
                    "metro_train": [],
                    "metro_tram": [{
                        "disruption_id": 143887,
                        "title": "Route 1: Temporary tram stop closure from Monday 23 July to late September 2018 ",
                        "url": "http://ptv.vic.gov.au/live-travel-updates/article/route-1-temporary-tram-stop-closure-from-monday-23-july-to-late-september-2018",
                        "description": "Route 1 trams (to South Melbourne) will not service the following stop from first service on Monday 23 July 2018 until late September 2018 due to tram infrastructure works on Sturt Street and on Southbank Boulevard.",
                        "disruption_status": "Current",
                        "disruption_type": "Planned Closure",
                        "published_on": null,
                        "last_updated": null,
                        "from_date": null,
                        "to_date": null,
                        "routes": []
                    }],
                    "metro_bus": [],
                    "regional_train": [],
                    "regional_coach": [],
                    "regional_bus": []
                },
                "status": {
                    "version": "3.0",
                    "health": 1
                }
          }
        """)

    @pytest.fixture(scope="module")
    def response_metro_bus(self):
        return json.loads("""
            {
                "disruptions": {
                    "general": [],
                    "metro_train": [],
                    "metro_tram": [],
                    "metro_bus": [{
                        "disruption_id": 145839,
                        "title": "Minor Delays to 10 min : Route: 382 Whittlesea - Northland SC via South Morang Station : to Whittlesea",
                        "url": "http://ptv.vic.gov.au/live-travel-updates/",
                        "description": "Minor Delays to 10 min : Route: 382 Whittlesea - Northland SC via South Morang Station : to Whittlesea",
                        "disruption_status": "Current",
                        "disruption_type": "Minor Delays",
                        "published_on": null,
                        "last_updated": null,
                        "from_date": null,
                        "to_date": null,
                        "routes": []
                    }],
                    "regional_train": [],
                    "regional_coach": [],
                    "regional_bus": []
                },
                "status": {
                    "version": "3.0",
                    "health": 1
                }
          }
        """)

    @pytest.fixture(scope="module")
    def response_regional_train(self):
        return json.loads("""
            {
                "disruptions": {
                    "general": [],
                    "metro_train": [],
                    "metro_tram": [],
                    "metro_bus": [],
                    "regional_train": [{
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
                    }],
                    "regional_coach": [],
                    "regional_bus": []
                },
                "status": {
                    "version": "3.0",
                    "health": 1
                }
          }
        """)

    def test_null(self, null_response):
        subject = DisruptionsResponse(null_response)
        assert len(subject.disruptions["general"]) == 0
        assert len(subject.disruptions["metro_train"]) == 0
        assert len(subject.disruptions["metro_tram"]) == 0
        assert len(subject.disruptions["metro_bus"]) == 0
        assert len(subject.disruptions["regional_train"]) == 0
        assert len(subject.disruptions["regional_coach"]) == 0
        assert len(subject.disruptions["regional_bus"]) == 0


    def test_metro_train(self, response_metro_train):
        subject = DisruptionsResponse(response_metro_train)
        assert len(subject.disruptions["metro_train"]) == 1
        assert subject.disruptions["metro_train"][0].__class__ == DisruptionResponse
        assert subject["metro_train"][0].__class__ == DisruptionResponse
        disruption = subject["metro_train"][0]

        assert disruption.id == 145833
        assert disruption.title == "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am."
        assert disruption.url == "http://ptv.vic.gov.au/live-travel-updates/"
        assert disruption.description == "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am."
        assert disruption.status == "Current"
        assert disruption.type == "Minor Delays"
        assert disruption.published_on == None
        assert disruption.last_updated == None
        assert disruption.from_date == None
        assert disruption.to_date == None
        assert len(disruption.routes) == 0

    def test_metro_train_with_dates(self, response_metro_train_with_dates):
        subject = DisruptionsResponse(response_metro_train_with_dates)
        assert len(subject.disruptions["metro_train"]) == 1
        assert subject.disruptions["metro_train"][0].__class__ == DisruptionResponse
        assert subject["metro_train"][0].__class__ == DisruptionResponse
        disruption = subject["metro_train"][0]

        assert disruption.id == 145833
        assert disruption.title == "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am."
        assert disruption.url == "http://ptv.vic.gov.au/live-travel-updates/"
        assert disruption.description == "The 8:44am Blackburn to Flinders Street service will terminate at Mont Albert due to a train fault. The next city bound service will depart from Mont Albert at 9:04am. The 9:09am Blackburn to Flinders Street service will originate from Box Hill this morning at 9:14am."
        assert disruption.status == "Current"
        assert disruption.type == "Minor Delays"
        assert disruption.published_on == datetime.datetime(2018, 8, 12, 22, 57, 10)
        assert disruption.last_updated == datetime.datetime(2018, 8, 12, 22, 58, 59)
        assert disruption.from_date == datetime.datetime(2018, 8, 12, 22, 56, 00)
        assert disruption.to_date == datetime.datetime(2018, 8, 14, 22, 56, 00)
        assert len(disruption.routes) == 0

    def test_metro_train_with_routes(self, response_metro_train_with_routes):
        subject = DisruptionsResponse(response_metro_train_with_routes)
        assert len(subject.disruptions["metro_train"]) == 1
        assert subject.disruptions["metro_train"][0].__class__ == DisruptionResponse
        assert subject["metro_train"][0].__class__ == DisruptionResponse
        disruption = subject["metro_train"][0]
        assert len(disruption.routes) == 1
        route = disruption.routes[0]

        assert route.type == TRAIN
        assert route.id == 2
        assert route.name == "Belgrave"
        assert route.number == ""
        assert route.gtfs_id == "2-BEL"
        assert route.direction.route_direction_id == 20
        assert route.direction.id == 1
        assert route.direction.name == "City (Flinders Street)"
        assert route.direction.service_time == None

    def test_metro_train_with_service_time(self, response_metro_train_with_service_time):
        subject = DisruptionsResponse(response_metro_train_with_service_time)
        assert len(subject.disruptions["metro_train"]) == 1
        assert subject.disruptions["metro_train"][0].__class__ == DisruptionResponse
        assert subject["metro_train"][0].__class__ == DisruptionResponse
        disruption = subject["metro_train"][0]
        assert len(disruption.routes) == 1
        route = disruption.routes[0]
        assert route.direction.service_time == datetime.datetime(1900, 1, 1, 12, 45, 0)

    def test_metro_tram(self, response_metro_tram):
        subject = DisruptionsResponse(response_metro_tram)
        assert len(subject.disruptions["metro_tram"]) == 1
        assert subject.disruptions["metro_tram"][0].__class__ == DisruptionResponse
        assert subject["metro_tram"][0].__class__ == DisruptionResponse
        disruption = subject["metro_tram"][0]

        assert disruption.id == 143887
        assert disruption.title == "Route 1: Temporary tram stop closure from Monday 23 July to late September 2018 "
        assert disruption.url == "http://ptv.vic.gov.au/live-travel-updates/article/route-1-temporary-tram-stop-closure-from-monday-23-july-to-late-september-2018"
        assert disruption.description == "Route 1 trams (to South Melbourne) will not service the following stop from first service on Monday 23 July 2018 until late September 2018 due to tram infrastructure works on Sturt Street and on Southbank Boulevard."
        assert disruption.status == "Current"
        assert disruption.type == "Planned Closure"
        assert disruption.published_on == None
        assert disruption.last_updated == None
        assert disruption.from_date == None
        assert disruption.to_date == None
        assert len(disruption.routes) == 0

    def test_metro_bus(self, response_metro_bus):
        subject = DisruptionsResponse(response_metro_bus)
        assert len(subject.disruptions["metro_bus"]) == 1
        assert subject.disruptions["metro_bus"][0].__class__ == DisruptionResponse
        assert subject["metro_bus"][0].__class__ == DisruptionResponse
        disruption = subject["metro_bus"][0]

        assert disruption.id == 145839
        assert disruption.title == "Minor Delays to 10 min : Route: 382 Whittlesea - Northland SC via South Morang Station : to Whittlesea"
        assert disruption.url == "http://ptv.vic.gov.au/live-travel-updates/"
        assert disruption.description == "Minor Delays to 10 min : Route: 382 Whittlesea - Northland SC via South Morang Station : to Whittlesea"
        assert disruption.status == "Current"
        assert disruption.type == "Minor Delays"
        assert disruption.published_on == None
        assert disruption.last_updated == None
        assert disruption.from_date == None
        assert disruption.to_date == None
        assert len(disruption.routes) == 0

    def test_regional_train(self, response_regional_train):
        subject = DisruptionsResponse(response_regional_train)
        assert len(subject.disruptions["regional_train"]) == 1
        assert subject.disruptions["regional_train"][0].__class__ == DisruptionResponse
        assert subject["regional_train"][0].__class__ == DisruptionResponse
        disruption = subject["regional_train"][0]

        assert disruption.id == 144252
        assert disruption.title == "Seymour line: Coaches replacing selected trains from Sunday 12 August to Wednesday 15 August 2018"
        assert disruption.url == "http://ptv.vic.gov.au/live-travel-updates/article/seymour-and-shepparton-lines-coaches-replacing-selected-trains-from-sunday-12-august-to-wednesday-15-august-2018"
        assert disruption.description == "Road coaches replace selected evening trains on the Seymour line from Sunday 12 August to Wednesday 15 August 2018, due to Metro track works."
        assert disruption.status == "Current"
        assert disruption.type == "Planned Works"
        assert disruption.published_on == None
        assert disruption.last_updated == None
        assert disruption.from_date == None
        assert disruption.to_date == None
        assert len(disruption.routes) == 0

    def test_status(self, response):
        subject = DisruptionsResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE


    def test_repr(self, response):
        subject = DisruptionsResponse(response)
        assert subject.__repr__().__class__ == str
