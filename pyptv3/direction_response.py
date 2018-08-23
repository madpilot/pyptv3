""" Provides the DirectionResponse Class """
from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class DirectionResponse:
    """
        Wraps the response from a Direction request
    """
    def __init__(self, response):
        self._direction_id = response["direction_id"]
        self._name = response["direction_name"]
        self._route_id = response["route_id"]
        self._route_type = response["route_type"]

    @property
    def direction_id(self):
        """
        Direction of travel identifier (int)
        """
        return self._direction_id


    @property
    def name(self):
        """
        Name of direction of travel (str)
        """
        return self._name

    @property
    def route_id(self):
        """
        Route identifier (int)
        """
        return self._route_id


    @property
    def route_type(self):
        """
        Transport mode identifier (TRAIN|TRAM|BUS|VLINE_TRAIN|NIGHT_BUS)
        """
        return self._route_type

    def __str__(self):
        return self.name

    def __repr__(self):
        if self.route_type == TRAIN:
            route_type = "TRAIN"
        elif self.route_type == TRAM:
            route_type = "TRAM"
        elif self.route_type == BUS:
            route_type = "BUS"
        elif self.route_type == VLINE_TRAIN:
            route_type = "VLINE_TRAIN"
        elif self.route_type == NIGHT_BUS:
            route_type = "NIGHT_BUS"

        return "<Direction direction_id:%r name:%r route_id:%r route_type:%r>" % \
                    (self.direction_id, self.name, self.route_id, route_type)
