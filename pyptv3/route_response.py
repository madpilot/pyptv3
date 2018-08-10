from pyptv3 import TRAIN, TRAM, BUS, VLINE_TRAIN, NIGHT_BUS

class RouteResponse:
    def __init__(self, response):
        self._id = response["route_id"]
        self._name = response["route_name"]
        self._type = response["route_type"]
        self._number = response["route_number"]
        self._gtfs_id = response["route_gtfs_id"]

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
    def number(self):
      return self._number

    @property
    def gtfs_id(self):
      return self._gtfs_id


    def __str__(self):
        return self.name

    def __repr__(self):
        if self.type == TRAIN:
            t = "TRAIN"
        elif self.type == TRAM:
            t = "TRAM"
        elif self.type == BUS:
            t = "BUS"
        elif self.type == VLINE_TRAIN:
            t = "VLINE_TRAIN"
        elif self.type == NIGHT_BUS:
            t = "NIGHT_BUS"

        return "<Route id:%i name:%s type:%s number:%s gtfs_id:%s>" %(self.id, self.name, t, self.number, self.gtfs_id)
