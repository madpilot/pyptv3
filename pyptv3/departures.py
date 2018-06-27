import pyptv3

class Departures:
    def __init__(self, client, route_type, stop_id):
        self._client = client
        self._route_type = route_type
        self._stop_id = stop_id

    def all(self, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get(self._base_path(), query_list)

    def by_route(self, route, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get(self._base_path() + "/route/" + str(route), query_list)

    def _base_path(self):
      return "/departures/route_type/" + str(self._route_type) + "/stop/" + str(self._stop_id)
