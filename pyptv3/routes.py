""" Provides the Routes Class """
import pyptv3

class Routes:
    """
        Access the Routes API
    """
    def __init__(self, client):
        self._client = client

    def all(self, **kwargs):
        """
        Route names and numbers for all routes of all route types.
        Return (pyptv.RoutesResponse)
        """
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return pyptv3.RoutesResponse(self._client.get("/routes", query_list))

    def by_id(self, route_id):
        """
        The route name and number for the specified route ID.

        Args:
            route_id: Identifier of route; values returned by Departures, Directions
                and Disruptions APIs
        Return (pyptv.RoutesResponse)
        """
        response = self._client.get("/routes/" + str(route_id))
        return pyptv3.RoutesResponse(response)
