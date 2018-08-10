class StopAmenityDetailsResponse:
    def __init__(self, response):
        self._toilet = response["toilet"]
        self._taxi_rank = response["taxi_rank"]
        self._car_parking = response["car_parking"]
        self._cctv = response["cctv"]

    @property
    def toilet(self):
        return self._toilet

    @property
    def taxi_rank(self):
        return self._taxi_rank

    @property
    def car_parking(self):
        return self._car_parking

    @property
    def cctv(self):
        return self._cctv


    def __repr__(self):
        return "<AmenityDetails toilet:%r taxi_rank:%r car_parking:%r cctv:%r>" %(self.toilet, self.taxi_rank, self.car_parking, self.cctv)
