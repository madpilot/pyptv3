from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class StopOnRouteResponse:
    def __init__(self, response):
        self._suburb = response["stop_suburb"]
        self._name = response["stop_name"]
        self._id = response["stop_id"]
        self._route_type = response["route_type"]
        self._latitude = response["stop_latitude"]
        self._longitude = response["stop_longitude"]
        self._sequence = response["stop_sequence"]

    @property
    def id(self):
      return self._id

    @property
    def name(self):
        return self._name.strip()

    @property
    def suburb(self):
        return self._suburb

    @property
    def route_type(self):
        return self._route_type

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def sequence(self):
        return self._sequence

    def __str__(self):
        return self.name

    def __repr__(self):
        if self.route_type == TRAIN:
            t = "TRAIN"
        elif self.route_type == TRAM:
            t = "TRAM"
        elif self.route_type == BUS:
            t = "BUS"
        elif self.route_type == VLINE_TRAIN:
            t = "VLINE_TRAIN"
        elif self.route_type == NIGHT_BUS:
            t = "NIGHT_BUS"

        return "<Route id:%i name:%s type:%s suburb:%s route_type:%s latitude:%f longitude:%f sequence:%i>" %(self.id, self.name, t, self.suburb, self.route_type, self.latitude, self.longitude, self.sequence)
