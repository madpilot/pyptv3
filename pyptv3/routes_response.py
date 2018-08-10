import pyptv3

class RoutesResponse():
    def __init__(self, response):
        self._routes = list(map(lambda t: pyptv3.RouteResponse(t), response["routes"]))
        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def routes(self):
        return self._routes

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return "<Routes routes:%r status:%r>" %(self.routes, self.status)

    def __getitem__(self, key):
        return self.routes[key]

    def __iter__(self):
        return self.routes.__iter__()

    def __len__(self):
        return self.routes.__len__()
