import pyptv3

class SingleDisruptionResponse():
    def __init__(self, response):
        self._disruption = pyptv3.DisruptionResponse(response["disruption"])
        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def disruption(self):
        return self._disruption

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return "<Disruption disruption:%r status:%r>" %(self.disruptions, self.status)

    def __getitem__(self, key):
        return self.disruption[key]

    def __iter__(self):
        return self.disruption.__iter__()

    def __len__(self):
        return self.disruption.__len__()

