import pyptv3

class Runs:
    def __init__(self, client):
        self._client = client

    def by_id(self, id, route_type = None, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        if route_type == None:
            return self._client.get("/runs/" + str(id), query_list)
        else:
            return self._client.get("/runs/" + str(id) + "/route_type/" + str(route_type), query_list)

    def by_route(self, route_id, route_type = None, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        if route_type == None:
            return self._client.get("/runs/route/" + str(route_id), query_list)
        else:
            return self._client.get("/runs/route/" + str(route_id) + "/route_type/" + str(route_type), query_list)
