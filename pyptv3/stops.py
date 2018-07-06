import pyptv3

class Stops:
    def __init__(self, client):
        self._client = client

    def by_stop(self, stop_id, route_type, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/stops/" + str(stop_id) + "/route_type/" + str(route_type), query_list)

    def by_route(self, route_id, route_type, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/stops/route/" + str(route_id) + "/route_type/" + str(route_type), query_list)

    def by_location(self, latitude, longitude, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/stops/location/" + str(latitude) + "," + str(longitude), query_list)
