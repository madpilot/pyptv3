class VehicleDescriptorResponse:
    def __init__(self, response):
        self._operator = response["operator"]
        self._id = response["id"]
        self._low_floor = response["low_floor"]
        self._air_conditioned = response["air_conditioned"]
        self._description = response["description"]
        self._supplier = response["supplier"]

    @property
    def operator(self):
        return self._operator

    @property
    def id(self):
        return self._id

    @property
    def low_floor(self):
        return self._low_floor

    @property
    def air_conditioned(self):
        return self._air_conditioned

    @property
    def description(self):
        return self._description

    @property
    def supplier(self):
        return self._supplier


    def __repr__(self):
        return "<VehicleDescriptor operator:%r id:%r low_floor:%r air_conditioned:%r description:%r supplier:%r>" % (self.operator, self.id, self.low_floor, self.air_conditioned, self.description, self.supplier)
