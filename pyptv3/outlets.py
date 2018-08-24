""" Provides the Outlets Class """
import pyptv3

class Outlets:
    """
    Fetch Outlets details

    Args:
        client (pyptv3.Client): Initialized client object
    """
    def __init__(self, client):
        self._client = client

    def all(self, **kwargs):
        """
        Ticket outlets.

        Returns:
          pyptv3.OutletsResponse
        """
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return pyptv3.OutletsResponse(self._client.get("/outlets", query_list))

    def by_location(self, latitude, longitude, **kwargs):
        """
        Ticket outlets near the specified location.

        Returns:
          pyptv3.OutletsGeolocationResponse
        """
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        path = "/outlets/location/" + str(latitude) + "," + str(longitude)
        response = self._client.get(path, query_list)
        return pyptv3.OutletsGeolocationResponse(response)
