""" Provides the Departures Class """
import pyptv3

class Departures:
    """
    Fetch Departure details

    Args:
        client (pyptv3.Client): Initialized client object
        route_type (int): Number identifying transport mode;
            values returned via a call to RouteTypes#get
        stop_id (int): Identifier of stop;
            values returned via a call to Stops API
    """
    def __init__(self, client, route_type, stop_id):
        self._client = client
        self._route_type = route_type
        self._stop_id = stop_id

    def all(self, **kwargs):
        """
        Service departures from the specified stop for all routes of the specified
        route type;
        departures are timetabled and real-time (if applicable).

        Returns:
            pyptv3.DeparturesResponse
        """
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return pyptv3.DeparturesResponse(self._client.get(self._base_path(), query_list))

    def by_route(self, route, **kwargs):
        """
        Service departures from the specified stop for the specified route
        (and route type);
        departures are timetabled and real-time (if applicable).

        Returns:
            pyptv3.DeparturesResponse
        """
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        path = self._base_path() + "/route/" + str(route)
        response = self._client.get(path, query_list)
        return pyptv3.DeparturesResponse(response)

    def _base_path(self):
        return "/departures/route_type/" \
            + str(self._route_type) \
            + "/stop/" \
            + str(self._stop_id)
