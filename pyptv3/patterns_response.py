""" Provides the PatternsResponse Class """
import pyptv3

class PatternsResponse: # pylint: disable=line-too-long,unnecessary-lambda
    """
        Wraps the response from a Patterns request
    """
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
        """
        Disruption information applicable to relevant routes or stops
        """
        return self._departures

    @property
    def stops(self):
        """
        A train station, tram stop, bus stop, regional coach stop or Night Bus stop
        """
        return self._stops


    @property
    def routes(self):
        """
        Train lines, tram routes, bus routes, regional coach routes, Night Bus routes
        """
        return self._routes

    @property
    def runs(self):
        """
        Individual trips/services of a route
        """
        return self._runs

    @property
    def directions(self):
        """
        Directions of travel of route
        """
        return self._directions

    @property
    def disruptions(self):
        """
        Disruption information applicable to relevant routes or stops
        """
        return self._disruptions


    @property
    def status(self):
        """
        API Status / Metadata
        """
        return self._status

    def __repr__(self):
        return "<Patterns departures:%r stops:%r routes:%r runs:%r directions:%r disruptions:%r status:%r>" %(self.departures, self.stops, self.routes, self.runs, self.directions, self.disruptions, self.status)
