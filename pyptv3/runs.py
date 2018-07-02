import pyptv3

class Runs:
    def __init__(self, client):
        self._client = client

    def by_id(self, id, route_type = None):
        if route_type == None:
            return self._client.get("/runs/" + str(id))
        else:
            return self._client.get("/runs/" + str(id) + "/route_type/" + str(route_type))

    def by_route(self, route_id, route_type = None):
        if route_type == None:
            return self._client.get("/runs/route/" + str(route_id))
        else:
            return self._client.get("/runs/route/" + str(route_id) + "/route_type/" + str(route_type))
