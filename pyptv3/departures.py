import pyptv3

class Departures:
    """
    Create a client class that will get passed in to other API object"

    Args:
        client (pyptv3.Client): Initialized client object
        route_type (int): Number identifying transport mode; values returned via a call to RouteTypes#get
        stop_id (int): Identifier of stop; values returned via a call to Stops API
    Returns:
        client: The initialized client object. Pass this in to the API classes
    """
    def __init__(self, client, route_type, stop_id):
        self._client = client
        self._route_type = route_type
        self._stop_id = stop_id

    """
    Service departures from the specified stop for all routes of the specified route type; departures are timetabled and real-time (if applicable).
    """
    def all(self, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get(self._base_path(), query_list)

    """
    Service departures from the specified stop for the specified route (and route type); departures are timetabled and real-time (if applicable).
    """
    def by_route(self, route, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get(self._base_path() + "/route/" + str(route), query_list)

    def _base_path(self):
      return "/departures/route_type/" + str(self._route_type) + "/stop/" + str(self._stop_id)
