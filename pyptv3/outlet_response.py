""" Provides the OutletGeolocationResponse Class """
class OutletResponse: # pylint: disable=line-too-long,too-many-instance-attributes
    """
        Wraps the response from a Outlet request
    """
    def __init__(self, response):
        self._outlet_id = response["outlet_slid_spid"]
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
    def outlet_id(self):
        """
        The SLID / SPID
        """
        return self._outlet_id

    @property
    def name(self):
        """
        The location name of the outlet
        """
        return self._name

    @property
    def business(self):
        """
        The business name of the outlet
        """
        return self._business

    @property
    def latitude(self):
        """
        Geographic coordinate of latitude at outlet
        """
        return self._latitude

    @property
    def longitude(self):
        """
        Geographic coordinate of longitude at outlet
        """
        return self._longitude

    @property
    def suburb(self):
        """
        The city/municipality the outlet is in
        """
        return self._suburb

    @property
    def postcode(self):
        """
        The postcode for the outlet
        """
        return self._postcode

    @property
    def business_hour_mon(self):
        """
        The business hours on Monday
        """
        return self._business_hour_mon

    @property
    def business_hour_tue(self):
        """
        The business hours on Tuesday
        """
        return self._business_hour_tue

    @property
    def business_hour_wed(self):
        """
        The business hours on Wednesday
        """
        return self._business_hour_wed

    @property
    def business_hour_thur(self):
        """
        The business hours on Thursday
        """
        return self._business_hour_thur

    @property
    def business_hour_fri(self):
        """
        The business hours on Friday
        """
        return self._business_hour_fri

    @property
    def business_hour_sat(self):
        """
        The business hours on Saturday
        """
        return self._business_hour_sat

    @property
    def business_hour_sun(self):
        """
        The business hours on Sunday
        """
        return self._business_hour_sun

    @property
    def notes(self):
        """
        Any additional notes for the outlet such as 'Buy pre-loaded myki cards only'. May be null/empty.Any additional notes for the outlet such as 'Buy pre-loaded myki cards only'. May be None or Empty.
        """
        return self._notes

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Outlet outlet_id:%r name:%r business:%r latitude:%r longitude:%r suburb:%r postcode:%r business_hour_mon:%r business_hour_tue:%r business_hour_wed:%r business_hour_thur:%r business_hour_fri:%r business_hour_sat:%r business_hour_sun:%r notes:%r>" %(self.outlet_id, self.name, self.business, self.latitude, self.longitude, self.suburb, self.postcode, self.business_hour_mon, self.business_hour_tue, self.business_hour_wed, self.business_hour_thur, self.business_hour_fri, self.business_hour_sat, self.business_hour_sun, self.notes)
