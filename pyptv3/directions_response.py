import pyptv3

class DirectionsResponse():
    def __init__(self, response):
        self._directions = list(map(lambda t: pyptv3.DirectionResponse(t), response["directions"]))
        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def directions(self):
        return self._directions

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return "<Directions directions:%r status:%r>" %(self.directions, self.status)

    def __getitem__(self, key):
        return self.directions[key]

    def __iter__(self):
        return self.directions.__iter__()

    def __len__(self):
        return self.directions.__len__()
