""" Provides the OutletsGeolocationResponse Class """
import pyptv3

class OutletsGeolocationResponse(pyptv3.OutletsResponse):
    """
        Wraps the response from a OutletsGeolocation request
    """
    def __init__(self, response):
        super().__init__(response)
        self._outlets = list(map(lambda t: pyptv3.OutletGeolocationResponse(t), response["outlets"])) # pylint: disable=line-too-long,unnecessary-lambda
        self._status = pyptv3.StatusResponse(response["status"])
