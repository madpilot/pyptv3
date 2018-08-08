import pyptv3

class RouteTypes:
    TRAIN = 0
    TRAM = 1
    BUS = 2
    VLINE_TRAIN = 3
    NIGHT_BUS = 4

    def __init__(self, client):
        self._client = client

    def all(self):
        return self._client.get("/route_types")
