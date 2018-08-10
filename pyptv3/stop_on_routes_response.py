import pyptv3

class StopOnRoutesResponse():
    def __init__(self, response):
        self._stops = list(map(lambda t: pyptv3.StopOnRouteResponse(t), response["stops"]))
        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def stops(self):
        return self._stops

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return "<StopOnRoutes stops:%r status:%r>" %(self.stops, self.status)

    def __getitem__(self, key):
        return self.stops[key]

    def __iter__(self):
        return self.stops.__iter__()

    def __len__(self):
        return self.stops.__len__()
