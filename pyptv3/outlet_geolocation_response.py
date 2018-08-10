import pyptv3

class OutletGeolocationResponse(pyptv3.OutletResponse):
    def __init__(self, response):
        super(OutletGeolocationResponse, self).__init__(response)
        self._distance = response["outlet_distance"]

    @property
    def distance(self):
        return self._distance

    def __repr__(self):
        return "<OutletGeolocationdistance:%i id:%s name:%s business:%s latitude:%s longitude:%s suburb:%s postcode:%i business_hour_mon:%s business_hour_tue:%s business_hour_wed:%s business_hour_thur:%s business_hour_fri:%s business_hour_sat:%s business_hour_sun:%s notes:%s>" %(self.distance, self.id, self.name, self.business, self.latitude, self.longitude, self.suburb, self.postcode, self.business_hour_mon, self.business_hour_tue, self.business_hour_wed, self.business_hour_thur, self.business_hour_fri, self.business_hour_sat, self.business_hour_sun, self.notes)
