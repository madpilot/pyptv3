import datetime

class DisruptionDirectionResponse:
    def __init__(self, response):
        self._id = response["direction_id"]
        self._name = response["direction_name"]
        self._route_direction_id = response["route_direction_id"]

        self._service_time = None
        if response["service_time"] is not None:
            self._service_time = self.parse_time(response["service_time"])

    def parse_time(self, time):
        return datetime.datetime.strptime(time, "%H:%M:%S")

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name


    @property
    def route_direction_id(self):
        return self._route_direction_id


    @property
    def service_time(self):
        return self._service_time

