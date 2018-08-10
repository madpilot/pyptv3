import pyptv3
from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS


class StopByDistanceResponse(pyptv3.StopOnRouteResponse):
    def __init__(self, response):
        super().__init__(response)
        self._distance = response["stop_distance"]

    @property
    def distance(self):
        return self._distance


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

        return "<Route distance:%s id:%i name:%s type:%s suburb:%s route_type:%s latitude:%f longitude:%f sequence:%i>" %(self.distance, self.id, self.name, t, self.suburb, self.route_type, self.latitude, self.longitude, self.sequence)
