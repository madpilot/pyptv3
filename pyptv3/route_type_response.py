class RouteTypeResponse:
    TRAIN = 0
    TRAM = 1
    BUS = 2
    VLINE_TRAIN = 3
    NIGHT_BUS = 4

    def __init__(self, response):
        self._name = response["route_type_name"]
        self._type = response["route_type"]

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    def __str__(self):
        return self.name

    def __repr__(self):
        if self.type == RouteTypeResponse.TRAIN:
            t = "TRAIN"
        elif self.type == RouteTypeResponse.TRAM:
            t = "TRAM"
        elif self.type == RouteTypeResponse.BUS:
            t = "BUS"
        elif self.type == RouteTypeResponse.VLINE_TRAIN:
            t = "VLINE_TRAIN"
        elif self.type == RouteTypeResponse.NIGHT_BUS:
            t = "NIGHT_BUS"

        return "<RouteType name:%s type:%s>" %(self.name, t)
