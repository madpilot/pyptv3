import pyptv3

class StopResponse:
    def __init__(self, response):
        self._details = pyptv3.StopDetailsResponse(response["stop"])
        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def details(self):
        return self._details

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return "<Stop details:%r status:%r>" %(self.details, self.status)
