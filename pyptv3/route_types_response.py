import pyptv3

class RouteTypesResponse():
    def __init__(self, response):
        self._types = list(map(lambda t: pyptv3.RouteTypeResponse(t), response["route_types"]))
        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def types(self):
        return self._types

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return "<RouteTypes types:%r status:%r>" %(self.types, self.status)

    def __getitem__(self, key):
        return self.types[key]

    def __iter__(self):
        return self.types.__iter__()

    def __len__(self):
        return self.types.__len__()
