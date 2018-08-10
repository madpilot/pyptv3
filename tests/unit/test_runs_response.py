import pytest
from mock import Mock
import json
from pyptv3 import RunsResponse, RunResponse, StatusResponse, ONLINE, TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class TestRoutes:
    @pytest.fixture(scope="module")
    def response(self):
        return json.loads("""
          {
            "runs": [
              {
                "run_id": 44076,
                "route_id": 13,
                "route_type": 0,
                "final_stop_id": 1185,
                "destination_name": "Stony Point ",
                "status": "scheduled",
                "direction_id": 12,
                "run_sequence": 0,
                "express_stop_count": 0,
                "vehicle_position": null,
                "vehicle_descriptor": null
              }
            ],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    @pytest.fixture(scope="module")
    def response_with_vehicle_position(self):
        return json.loads("""
          {
            "runs": [
              {
                "run_id": 44076,
                "route_id": 13,
                "route_type": 0,
                "final_stop_id": 1185,
                "destination_name": "Stony Point ",
                "status": "scheduled",
                "direction_id": 12,
                "run_sequence": 0,
                "express_stop_count": 0,
                "vehicle_position": {
                    "latitude": 37.8136,
                    "longitude": 144.9631,
                    "bearing": 90,
                    "supplier": "ACME Data"
                },
                "vehicle_descriptor": null
              }
            ],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    @pytest.fixture(scope="module")
    def response_with_vehicle_descriptor(self):
        return json.loads("""
          {
            "runs": [
              {
                "run_id": 44076,
                "route_id": 13,
                "route_type": 0,
                "final_stop_id": 1185,
                "destination_name": "Stony Point ",
                "status": "scheduled",
                "direction_id": 12,
                "run_sequence": 0,
                "express_stop_count": 0,
                "vehicle_position": null,
                "vehicle_descriptor": {
                  "operator": "Metro Trains Melbourne",
                  "id": 26094,
                  "low_floor": null,
                  "air_conditioned": null,
                  "description": "3 Car Siemens",
                  "supplier": "ACME Data"
                }
              },
              {
                "run_id": 4496,
                "route_id": 724,
                "route_type": 1,
                "final_stop_id": 2931,
                "destination_name": "Cotham Rd/Glenferrie Rd #80 ",
                "status": "scheduled",
                "direction_id": 11,
                "run_sequence": 0,
                "express_stop_count": 0,
                "vehicle_position": null,
                "vehicle_descriptor": {
                  "operator": "Yarra Trams",
                  "id": 26095,
                  "low_floor": true,
                  "air_conditioned": true,
                  "description": null,
                  "supplier": "ACME Data"
                }
              }
            ],
            "status": {
              "version": "3.0",
              "health": 1
            }
          }
        """)

    def test_runs(self, response):
        subject = RunsResponse(response)
        assert len(subject.runs) == 1

        assert subject.runs[0].__class__ == RunResponse
        assert subject[0].__class__ == RunResponse

        assert subject.runs[0].run_id == 44076
        assert subject.runs[0].route_id == 13
        assert subject.runs[0].route_type == TRAIN
        assert subject.runs[0].final_stop_id == 1185
        assert subject.runs[0].destination_name == "Stony Point"
        assert subject.runs[0].status == "scheduled"
        assert subject.runs[0].direction_id == 12
        assert subject.runs[0].run_sequence == 0
        assert subject.runs[0].express_stop_count == 0
        assert subject.runs[0].vehicle_position == None
        assert subject.runs[0].vehicle_descriptor == None

    def test_runs_with_vehicle_position(self, response_with_vehicle_position):
        subject = RunsResponse(response_with_vehicle_position)
        assert subject.runs[0].vehicle_position.latitude == 37.8136
        assert subject.runs[0].vehicle_position.longitude == 144.9631
        assert subject.runs[0].vehicle_position.bearing == 90
        assert subject.runs[0].vehicle_position.supplier == "ACME Data"

    def test_runs_with_vehicle_descriptor(self, response_with_vehicle_descriptor):
        subject = RunsResponse(response_with_vehicle_descriptor)
        assert subject.runs[0].vehicle_descriptor.operator == "Metro Trains Melbourne"
        assert subject.runs[0].vehicle_descriptor.id == 26094
        assert subject.runs[0].vehicle_descriptor.low_floor == None
        assert subject.runs[0].vehicle_descriptor.air_conditioned == None
        assert subject.runs[0].vehicle_descriptor.description == "3 Car Siemens"
        assert subject.runs[0].vehicle_descriptor.supplier == "ACME Data"

        assert subject.runs[1].vehicle_descriptor.operator == "Yarra Trams"
        assert subject.runs[1].vehicle_descriptor.id == 26095
        assert subject.runs[1].vehicle_descriptor.low_floor == True
        assert subject.runs[1].vehicle_descriptor.air_conditioned == True
        assert subject.runs[1].vehicle_descriptor.description == None
        assert subject.runs[1].vehicle_descriptor.supplier == "ACME Data"

    def test_status(self, response):
        subject = RunsResponse(response)
        assert subject.status.__class__ == StatusResponse
        assert subject.status.version == "3.0"
        assert subject.status.health == ONLINE

