import datetime

class DepartureResponse:
    def __init__(self, response):
        self._stop_id = response["stop_id"]
        self._route_id = response["route_id"]
        self._run_id = response["run_id"]
        self._direction_id = response["direction_id"]
        self._disruption_ids = response["disruption_ids"]
        self._scheduled_departure = None

        if response["scheduled_departure_utc"]:
            self._scheduled_departure = self.parse_datetime(response["scheduled_departure_utc"])

        self._estimated_departure = None
        if response["estimated_departure_utc"]:
            self._estimated_departure = self.parse_datetime(response["estimated_departure_utc"])

        self._at_platform = response["at_platform"]
        self._platform_number = response["platform_number"]
        self._flags = response["flags"]
        self._sequence = response["departure_sequence"]

    def parse_datetime(self, dt):
        return datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%SZ")

    @property
    def stop_id(self):
        return self._stop_id

    @property
    def route_id(self):
        return self._route_id

    @property
    def run_id(self):
        return self._run_id

    @property
    def direction_id(self):
        return self._direction_id

    @property
    def disruption_ids(self):
        return self._disruption_ids

    @property
    def scheduled_departure(self):
        return self._scheduled_departure

    @property
    def estimated_departure(self):
        return self._estimated_departure

    @property
    def at_platform(self):
        return self._at_platform

    @property
    def platform_number(self):
        return self._platform_number

    @property
    def flags(self):
        return self._flags

    @property
    def sequence(self):
        return self._sequence

    def __repr__(self):
        return "<Departure stop_id:%r route_id:%r run_id:%r direction_id:%r disruption_ids: %r scheduled_departure:%r estimated_departure:%r at_platform:%r platform_number:%r flags:%r sequence:%r>" %(self.stop_id, self.route_id, self.run_id, self.direction_id, self._disruption_ids, self.scheduled_departure, self.estimated_departure, self.at_platform, self.platform_number, self.flags, self.sequence)
