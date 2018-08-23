import pyptv3

class PatternsResponse:
    def __init__(self, response):
        self._departures = list(map(lambda d: pyptv3.DepartureResponse(d), response["departures"]))

        self._stops = dict(map(lambda kv: (kv[0], pyptv3.StopByDistanceResponse(kv[1])), response["stops"].items()))
        self._routes = dict(map(lambda kv: (kv[0], pyptv3.RouteResponse(kv[1])), response["routes"].items()))
        self._runs = dict(map(lambda kv: (kv[0], pyptv3.RunResponse(kv[1])), response["runs"].items()))
        self._directions = dict(map(lambda kv: (kv[0], pyptv3.DirectionResponse(kv[1])), response["directions"].items()))
        self._disruptions = list(map(lambda d: pyptv3.DisruptionResponse(d), response["disruptions"]))

        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def departures(self):
        return self._departures

    @property
    def stops(self):
        return self._stops


    @property
    def routes(self):
        return self._routes

    @property
    def runs(self):
        return self._runs

    @property
    def directions(self):
        return self._directions

    @property
    def disruptions(self):
        return self._disruptions

    @property
    def departures(self):
        return self._departures

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return "<Patterns departures:%r stops:%r routes:%r runs:%r directions:%r disruptions:%r status:%r>" %(self.departures, self.stops, self.routes, self.runs, self.directions, self.disruptions, self.status)

