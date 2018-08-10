class VehiclePositionResponse:
    def __init__(self, response):
        self._latitude = response["latitude"]
        self._longitude = response["longitude"]
        self._bearing = response["bearing"]
        self._supplier = response["supplier"]

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def bearing(self):
        return self._bearing

    @property
    def supplier(self):
        return self._supplier


    def __repr__(self):
        return "<VehiclePositionResponse latitude:%f longitude:%f bearing:%f supplier:%s>" %(self.latitude, self.longitude, bearing, supplier)
