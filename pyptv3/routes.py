import pyptv3

class Routes:
    def __init__(self, client):
        self._client = client

    def all(self, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return pyptv3.RoutesResponse(self._client.get("/routes", query_list))

    def by_id(self, id):
        return pyptv3.RoutesResponse(self._client.get("/routes/" + str(id)))
