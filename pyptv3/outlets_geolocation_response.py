import pyptv3

class OutletsGeolocationResponse(pyptv3.OutletsResponse):
    def __init__(self, response):
        super().__init__(response)
        self._outlets = list(map(lambda t: pyptv3.OutletGeolocationResponse(t), response["outlets"]))
        self._status = pyptv3.StatusResponse(response["status"])
