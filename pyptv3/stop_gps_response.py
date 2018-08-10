class StopGpsResponse:
    def __init__(self, response):
        self._latitude = response["latitude"]
        self._longitude = response["longitude"]

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def __repr__(self):
        return "<Gps latitude:%r longitude:%r>" %(self.latitude, self.longitude)
