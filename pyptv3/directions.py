import pyptv3

class Directions:
    def __init__(self, client):
        self._client = client

    def by_id(self, id, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/directions/" + str(id), query_list)

    def by_route(self, route_id, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/directions/route/" + str(route_id), query_list)

    def by_route_type(self, id, route_type, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/directions/" + str(id) + "/route_type/" + str(route_type), query_list)
