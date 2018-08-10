import pyptv3

class StopsByDistanceResponse(pyptv3.StopOnRoutesResponse):
    def __init__(self, response):
        self._stops = list(map(lambda t: pyptv3.StopByDistanceResponse(t), response["stops"]))
        self._status = pyptv3.StatusResponse(response["status"])

def __repr__(self):
        return "<StopsByDistance stops:%r status:%r>" %(self.stops, self.status)
