""" Provides the RouteTypes Class """
import pyptv3

class RouteTypes: # pylint: disable=too-few-public-methods
    """
    View all route types and their names
    """
    def __init__(self, client):
        self._client = client

    def all(self):
        """
        All route types (i.e. identifiers of transport modes) and their names.
        """
        return pyptv3.RouteTypesResponse(self._client.get("/route_types"))
