""" Provides the DeparturesResponse Class """
import pyptv3

class DeparturesResponse: # pylint: disable=unnecessary-lambda,line-too-long
    """
        Wraps the response from a Departures request
    """
    def __init__(self, response):
        self._departures = list(map(lambda t: \
            pyptv3.DepartureResponse(t), response["departures"]))

        self._stops = dict(map(lambda kv: \
            (kv[0], pyptv3.StopByDistanceResponse(kv[1])), response["stops"].items()))

        self._routes = dict(map(lambda kv: \
            (kv[0], pyptv3.RouteResponse(kv[1])), response["routes"].items()))

        self._runs = dict(map(lambda kv: \
            (kv[0], pyptv3.RunResponse(kv[1])), response["runs"].items()))

        self._directions = dict(map(lambda kv: \
            (kv[0], pyptv3.DirectionResponse(kv[1])), response["directions"].items()))


        self._disruptions = dict(map(lambda kv: \
            (kv[0], pyptv3.DisruptionResponse(kv[1])), response["disruptions"].items()))

        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def departures(self):
        """
        Timetabled and real-time service departures

        Returns:
            list: pyptv3.Departure
        """
        return self._departures

    @property
    def stops(self):
        """
        A train station, tram stop, bus stop, regional coach stop or Night Bus stop

        Returns:
            dict: keys=int, values=pyptv3.StopResponse - the key is the stop identifier
        """
        return self._stops


    @property
    def routes(self):
        """
        Train lines, tram routes, bus routes, regional coach routes, Night Bus routes

        Returns:
            dict: keys=int, values=pyptv3.RouteResponse - the key is the route identifier
        """
        return self._routes

    @property
    def runs(self):
        """
        Individual trips/services of a route

        Returns:
            dict: keys=int, values=pyptv3.RunResponse - the key is the run identifier
        """
        return self._runs

    @property
    def directions(self):
        """
        Directions of travel of route

        Returns:
            dict: keys=int, values=pyptv3.DirectionResponse - the key is the direction identifier
        """
        return self._directions

    @property
    def disruptions(self):
        """
        Disruption information applicable to relevant routes or stops

        Returns:
            dict: keys=int, values=pyptv3.DirectionResponse - the key is the disruption identifier
        """
        return self._disruptions

    @property
    def status(self):
        """
        API Status object

        Returns:
            pyptv3.Status
        """
        return self._status

    def __repr__(self):
        return "<Departures departures:%r stops:%r routes:%r runs:%r directions:%r disruptions:%r status:%r>" % \
                            (self.departures, self.stops, self.routes, self.runs, self.directions, self.disruptions, self.status)

    def __getitem__(self, key):
        return self.departures[key]

    def __iter__(self):
        return self.departures.__iter__()

    def __len__(self):
        return self.departures.__len__()
