import pyptv3

class RouteTypes:
    def __init__(self, client):
        self._client = client

    def all(self):
        return self._client.get("/route_types")
