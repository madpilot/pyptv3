""" Provides the RouteResponse Class """
from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class RouteResponse: # pylint: disable=line-too-long
    """
        Wraps the response from a Route request
    """
    def __init__(self, response):
        self._route_id = response["route_id"]
        self._name = response["route_name"]
        self._type = response["route_type"]
        self._number = response["route_number"]
        self._gtfs_id = response["route_gtfs_id"]

    @property
    def route_id(self):
        """
        Route identifier (int)
        """
        return self._route_id

    @property
    def name(self):
        """
        Name of route (str)
        """
        return self._name

    @property
    def type(self):
        """
        Transport mode identifier (TRAIN|TRAM|BUS|VLINE_TRAIN|NIGHT_BUS)
        """
        return self._type

    @property
    def number(self):
        """
        Route number presented to public (nb. not route_id) (str)
        """
        return self._number

    @property
    def gtfs_id(self):
        """
        GTFS Identifer of the route (str)
        """
        return self._gtfs_id


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

        return "<Route id:%r name:%r type:%r number:%r gtfs_id:%r>" %(self.route_id, self.name, route_type, self.number, self.gtfs_id)
