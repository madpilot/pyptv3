from pyptv3 import ONLINE, OFFLINE

class StatusResponse:
    def __init__(self, response):
        self._version = response["version"]
        self._health = response["health"]

    @property
    def version(self):
      return self._version

    @property
    def health(self):
        return self._health

    def __str__(self):
        if self.health == OFFLINE:
            return "OFFLINE"
        elif self.health == ONLINE:
            return "ONLINE"

    def __repr__(self):
        health = "OFFLINE"
        if self.health == ONLINE:
            health == "ONLINE"

        return "<Status version:%r health:%r>" %(self.version, str(self))

