import pyptv3

class StopDetailsResponse:
    def __init__(self, response):
        self._id = response["stop_id"]
        self._name = response["stop_name"]
        self._type = response["station_type"]
        self._description = response["station_description"]
        self._route_type = response["route_type"]

        self._location = None
        self._amenities = None
        self._accessibility = None

        if response["stop_location"] is not None:
            self._location = pyptv3.StopLocationResponse(response["stop_location"])

        if response["stop_amenities"] is not None:
            self._amenities = pyptv3.StopAmenityDetailsResponse(response["stop_amenities"])

        if response["stop_accessibility"] is not None:
            self._accessibility = pyptv3.StopAccessibilityResponse(response["stop_accessibility"])

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def description(self):
        return self._description

    @property
    def route_type(self):
        return self._route_type

    @property
    def location(self):
        return self._location

    @property
    def amenities(self):
        return self._amenities

    @property
    def accessibility(self):
        return self._accessibility


    def __repr__(self):
        return "<StopDetails id:%r, name:%r, type: %r, description: %r, route_type:%r, location:%r, amenities:%r, accessibility:%r>" %(self.id, self.name, self.type, self.description, self.route_type, self.location, self.amenities, self.accessibility)
