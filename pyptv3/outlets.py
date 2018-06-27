import pyptv3

class Outlets:
    def __init__(self, client):
        self._client = client

    def all(self, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/outlets", query_list)

    def by_location(self, latitude, longitude, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/outlets/location/" + str(latitude) + "," + str(longitude), query_list)
