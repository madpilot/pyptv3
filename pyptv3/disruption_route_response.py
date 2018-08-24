""" Provides the DisruptionRouteResponse Class """
import pyptv3
from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class DisruptionRouteResponse(pyptv3.RouteResponse):
    """
        Wraps the response from a DisruptionRoute request
    """
    def __init__(self, response):
        super().__init__(response)
        self._direction = None

        if response["direction"] is not None:
            self._direction = pyptv3.DisruptionDirectionResponse(response["direction"])

    @property
    def direction(self):
        """
        Direction of travel relevant to a disruption (if applicable) (pyptv3.DisruptionDirection)
        """
        return self._direction

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

        return "<DisruptionRoute route_id:%r name:%r type:%r number:%r gtfs_id:%r direction:%r>" %(self.route_id, self.name, route_type, self.number, self.gtfs_id, self.direction) # pylint: disable=line-too-long
