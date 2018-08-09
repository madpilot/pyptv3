from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class RouteTypeResponse:
    def __init__(self, response):
        self._name = response["route_type_name"]
        self._type = response["route_type"]

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    def __str__(self):
        return self.name

    def __repr__(self):
        if self.type == TRAIN:
            t = "TRAIN"
        elif self.type == TRAM:
            t = "TRAM"
        elif self.type == BUS:
            t = "BUS"
        elif self.type == VLINE_TRAIN:
            t = "VLINE_TRAIN"
        elif self.type == NIGHT_BUS:
            t = "NIGHT_BUS"

        return "<RouteType name:%s type:%s>" %(self.name, t)
