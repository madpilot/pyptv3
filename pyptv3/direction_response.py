from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class DirectionResponse:
    def __init__(self, response):
        self._id = response["direction_id"]
        self._name = response["direction_name"]
        self._route_id = response["route_id"]
        self._route_type = response["route_type"]

    @property
    def id(self):
        return self._id


    @property
    def name(self):
        return self._name

    @property
    def route_id(self):
        return self._route_id


    @property
    def route_type(self):
        return self._route_type

    def __str__(self):
        return self.name

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

        return "<DirectionResponse id:%r name:%r route_id:%r route_type:%r>" %(self.id, self.name, self.route_id, t)
