import pyptv3

class Disruptions:
    def __init__(self, client):
        self._client = client

    def all(self, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/disruptions", query_list)

    def by_route(self, route_id, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/disruptions/route/" + str(route_id), query_list)

    def by_id(self, id):
        return self._client.get("/disruptions/" + str(id))
