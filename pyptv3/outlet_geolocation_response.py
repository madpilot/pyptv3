import pyptv3

class OutletGeolocationResponse(pyptv3.OutletResponse):
    def __init__(self, response):
        super().__init__(response)
        self._distance = response["outlet_distance"]

    @property
    def distance(self):
        return self._distance

    def __repr__(self):
        return "<OutletGeolocationdistance:%r id:%r name:%r business:%r latitude:%r longitude:%r suburb:%r postcode:%r business_hour_mon:%r business_hour_tue:%r business_hour_wed:%r business_hour_thur:%r business_hour_fri:%r business_hour_sat:%r business_hour_sun:%r notes:%r>" %(self.distance, self.id, self.name, self.business, self.latitude, self.longitude, self.suburb, self.postcode, self.business_hour_mon, self.business_hour_tue, self.business_hour_wed, self.business_hour_thur, self.business_hour_fri, self.business_hour_sat, self.business_hour_sun, self.notes)
