from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class OutletResponse:
    def __init__(self, response):
        self._id = response["outlet_slid_spid"]
        self._name = response["outlet_name"]
        self._business = response["outlet_business"]
        self._latitude = response["outlet_latitude"]
        self._longitude = response["outlet_longitude"]
        self._suburb = response["outlet_suburb"]
        self._postcode = response["outlet_postcode"]
        self._business_hour_mon = response["outlet_business_hour_mon"]
        self._business_hour_tue = response["outlet_business_hour_tue"]
        self._business_hour_wed = response["outlet_business_hour_wed"]
        self._business_hour_thur = response["outlet_business_hour_thur"]
        self._business_hour_fri = response["outlet_business_hour_fri"]
        self._business_hour_sat = response["outlet_business_hour_sat"]
        self._business_hour_sun = response["outlet_business_hour_sun"]
        self._notes = response["outlet_notes"]

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def business(self):
        return self._business

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def suburb(self):
        return self._suburb

    @property
    def postcode(self):
        return self._postcode

    @property
    def business_hour_mon(self):
        return self._business_hour_mon

    @property
    def business_hour_tue(self):
        return self._business_hour_tue

    @property
    def business_hour_wed(self):
        return self._business_hour_wed

    @property
    def business_hour_thur(self):
        return self._business_hour_thur

    @property
    def business_hour_fri(self):
        return self._business_hour_fri

    @property
    def business_hour_sat(self):
        return self._business_hour_sat

    @property
    def business_hour_sun(self):
        return self._business_hour_sun

    @property
    def notes(self):
        return self._notes

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Outlet id:%s name:%s business:%s latitude:%s longitude:%s suburb:%s postcode:%i business_hour_mon:%s business_hour_tue:%s business_hour_wed:%s business_hour_thur:%s business_hour_fri:%s business_hour_sat:%s business_hour_sun:%s notes:%s>" %(self.id, self.name, self.business, self.latitude, self.longitude, self.suburb, self.postcode, self.business_hour_mon, self.business_hour_tue, self.business_hour_wed, self.business_hour_thur, self.business_hour_fri, self.business_hour_sat, self.business_hour_sun, self.notes)
