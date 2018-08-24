""" Provides the Disruptions Class """
import pyptv3

class Disruptions:
    """
    Fetch Disruptions details

    Args:
        client (pyptv3.Client): Initialized client object
    """
    def __init__(self, client):
        self._client = client

    def all(self, **kwargs):
        """
        All disruption information for all route types.

        Returns:
          pyptv3.DisruptionsResponse
        """
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        response = self._client.get("/disruptions", query_list)
        return pyptv3.DisruptionsResponse(response)

    def by_route(self, route_id, **kwargs):
        """
        All disruption information (if any exists) for the specified route.

        Args:
            route_id (int): Disruption id

        Returns:
          pyptv3.SingleDisruptionResponse
        """
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        response = self._client.get("/disruptions/route/" + str(route_id), query_list)
        return pyptv3.DisruptionsResponse(response)

    def by_id(self, disruption_id):
        """
        Disruption information for the specified disruption ID.

        Args:
            id (int): Disruption id

        Returns:
          pyptv3.SingleDisruptionResponse
        """
        response = self._client.get("/disruptions/" + str(disruption_id))
        return pyptv3.SingleDisruptionResponse(response)
