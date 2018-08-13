import pyptv3

class DeparturesResponse:
    def __init__(self, response):
        self._departures = list(map(lambda t: pyptv3.DepartureResponse(t), response["departures"]))
        self._stops = {}
        self._routes = {}
        self._runs = {}
        self._directions = {}
        self._diruptions = {}
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
    def status(self):
        return self._status

    def __repr__(self):
        return "<DeparturesResponse departures:%r status:%r>" %(self.departures, self.status)

    def __getitem__(self, key):
        return self.departures[key]

    def __iter__(self):
        return self.departures.__iter__()

    def __len__(self):
        return self.departures.__len__()

