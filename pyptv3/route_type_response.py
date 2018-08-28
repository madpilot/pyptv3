""" Provides the RouteTypeResponse Class """
from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class RouteTypeResponse:
    """
        Wraps the response from a RouteType request
    """
    def __init__(self, response):
        self._name = response["route_type_name"]
        self._type = response["route_type"]

    @property
    def name(self):
        """
        Name of transport mode
        """
        return self._name

    @property
    def type(self):
        """
        Transport mode identifier (TRAIN|TRAM|BUS|VLINE_TRAIN|NIGHT_BUS)
        """
        return self._type

    def __str__(self):
        return self.name

    def __repr__(self):
        if self.type == TRAIN:
            route_type = "TRAIN"
        elif self.type == TRAM:
            route_type = "TRAM"
        elif self.type == BUS:
            route_type = "BUS"
        elif self.type == VLINE_TRAIN:
            route_type = "VLINE_TRAIN"
        elif self.type == NIGHT_BUS:
            route_type = "NIGHT_BUS"

        return "<RouteType name:%r type:%r>" %(self.name, route_type)
