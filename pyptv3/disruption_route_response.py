import pyptv3

class DisruptionRouteResponse(pyptv3.RouteResponse):
    def __init__(self, response):
        super().__init__(response)
        self._direction = None

        if response["direction"] is not None:
            self._direction = pyptv3.DisruptionDirectionResponse(response["direction"])

    @property
    def direction(self):
        return self._direction

    def __repr__(self):
        return "<DisruptionRoute direction:%r routes:%r status:%r>" %(self.direction, self.routes, self.status)


