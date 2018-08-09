class StatusResponse:
    ONLINE = 1
    OFFLINE = 0

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
        if self.health == StatusResponse.OFFLINE:
            return "OFFLINE"
        elif self.health == StatusResponse.ONLINE:
            return "ONLINE"

    def __repr__(self):
        health = "OFFLINE"
        if self.health == 1:
            health == "ONLINE"

        return "<Status version:%s health:%s>" %(self.version, str(self))

