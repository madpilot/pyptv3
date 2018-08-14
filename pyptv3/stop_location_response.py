import pyptv3

class StopLocationResponse:
    def __init__(self, response):
        self._gps = pyptv3.StopGpsResponse(response["gps"])

    @property
    def gps(self):
        return self._gps

    def __repr__(self):
        return "<StopLocation gps:%r>" %(self.gps)
