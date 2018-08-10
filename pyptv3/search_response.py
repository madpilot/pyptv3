import pyptv3

class SearchResponse:
    def __init__(self, response):
        self._stops = None
        self._routes = None
        self._outlets = None
        self._status = pyptv3.StatusResponse(response["status"])

        if response["stops"] is not None:
            self._stops = pyptv3.StopsByDistanceResponse(response)

        if response["routes"] is not None:
            self._routes = pyptv3.RoutesResponse(response)

        if response["outlets"] is not None:
            self._outlets = pyptv3.OutletsGeolocationResponse(response)

    @property
    def stops(self):
        return self._stops

    @property
    def routes(self):
        return self._routes

    @property
    def outlets(self):
        return self._outlets

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return "<Search stops:%r routes:%r outlets:%r status:%r>" %(self.stops, self.routes, self.outlets, self.status)
