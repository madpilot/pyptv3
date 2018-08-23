""" Provides the Direction Class """
import pyptv3

class Directions:
    """
    Fetch Directions details

    Args:
        client (pyptv3.Client): Initialized client object
    """
    def __init__(self, client):
        self._client = client

    def by_id(self, direction_id):
        """
        All routes that travel in the specified direction.

        Args:
            direction_id (int): A direction id

        Returns:
          pyptv3.DirectionsResponse
        """
        response = self._client.get("/directions/" + str(direction_id))
        return pyptv3.DirectionsResponse(response)

    def by_route(self, route_id):
        """
        The directions that a specified route travels in.

        Args:
            route_id (int): A route id

        Returns:
          pyptv3.DirectionsResponse
        """
        response = self._client.get("/directions/route/" + str(route_id))
        return pyptv3.DirectionsResponse(response)

    def by_route_type(self, direction_id, route_type):
        """
        All routes of the specified route type that travel in the specified direction.

        Args:
            direction_id (int): A direction id
            route_type (TRAIN|TRAM|BUS|VLINE_TRAIN|NIGHT_BUS): The route type

        Returns:
          pyptv3.DirectionsResponse
        """
        response = self._client.get("/directions/" + \
            str(direction_id) + \
            "/route_type/" + \
            str(route_type))
        return pyptv3.DirectionsResponse(response)
