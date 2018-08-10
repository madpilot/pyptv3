from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS
import pyptv3

class RunResponse:
    def __init__(self, response):
        self._run_id = response["run_id"]
        self._route_id = response["route_id"]
        self._route_type = response["route_type"]
        self._final_stop_id = response["final_stop_id"]
        self._destination_name = response["destination_name"]
        self._status = response["status"]
        self._direction_id = response["direction_id"]
        self._run_sequence = response["run_sequence"]
        self._express_stop_count = response["express_stop_count"]
        self._vehicle_position = None
        if response["vehicle_position"] is not None:
            self._vehicle_position = pyptv3.VehiclePositionResponse(response["vehicle_position"])
        self._vehicle_descriptor = None
        if response["vehicle_descriptor"] is not None:
            self._vehicle_descriptor = pyptv3.VehicleDescriptorResponse(response["vehicle_descriptor"])

    @property
    def run_id(self):
        return self._run_id

    @property
    def route_id(self):
        return self._route_id

    @property
    def route_type(self):
          return self._route_type

    @property
    def final_stop_id(self):
          return self._final_stop_id

    @property
    def destination_name(self):
          return self._destination_name.strip()

    @property
    def status(self):
          return self._status

    @property
    def direction_id(self):
          return self._direction_id

    @property
    def run_sequence(self):
        return self._run_sequence

    @property
    def express_stop_count(self):
        return self._express_stop_count

    @property
    def vehicle_position(self):
        return self._vehicle_position

    @property
    def vehicle_descriptor(self):
        return self._vehicle_descriptor

    def __str__(self):
        return self.destination_name

    def __repr__(self):
        if self.route_type == TRAIN:
            t = "TRAIN"
        elif self.route_type == TRAM:
            t = "TRAM"
        elif self.route_type == BUS:
            t = "BUS"
        elif self.route_type == VLINE_TRAIN:
            t = "VLINE_TRAIN"
        elif self.route_type == NIGHT_BUS:
            t = "NIGHT_BUS"

        return "<Run run_id:%r route_id:%r route_type:%r final_stop_id:%r destination_name:%r status:%r direction_id:%r, run_sequence:%r express_stop_count:%r vehicle_position:%r vehicle_descriptor:%r>" % (self.run_id, self.route_id, t, self.final_stop_id, self.destination_name, self.status, self.direction_id, self.run_sequence, self.express_stop_count, self.vehicle_position, self.vehicle_descriptor)
