import pyptv3

class Directions:
    def __init__(self, client):
        self._client = client

    def by_id(self, id):
        return self._client.get("/directions/" + str(id))

    def by_route(self, route_id):
        return self._client.get("/directions/route/" + str(route_id))

    def by_route_type(self, id, route_type):
        return self._client.get("/directions/" + str(id) + "/route_type/" + str(route_type))
