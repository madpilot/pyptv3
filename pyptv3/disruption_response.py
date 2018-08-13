import pyptv3
import datetime

class DisruptionResponse:
    def __init__(self, response):
        self._id = response["disruption_id"]
        self._title = response["title"]
        self._url = response["url"]
        self._description = response["description"]
        self._status = response["disruption_status"]
        self._type = response["disruption_type"]

        self._published_on = None
        self._last_updated = None
        self._from_date = None
        self._to_date = None

        if response["published_on"] is not None:
            self._published_on = self.parse_datetime(response["published_on"])

        if response["last_updated"] is not None:
            self._last_updated = self.parse_datetime(response["last_updated"])

        if response["from_date"] is not None:
            self._from_date = self.parse_datetime(response["from_date"])

        if response["to_date"] is not None:
            self._to_date = self.parse_datetime(response["to_date"])

        self._routes = []
        if response["routes"] is not None:
            self._routes = list(map(lambda t: pyptv3.DisruptionRouteResponse(t), response["routes"]))

    def parse_datetime(self, dt):
        return datetime.datetime.strptime(dt, "%Y-%m-%dT%H:%M:%SZ")

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    @property
    def description(self):
        return self._description

    @property
    def status(self):
        return self._status

    @property
    def type(self):
        return self._type

    @property
    def published_on(self):
        return self._published_on

    @property
    def last_updated(self):
        return self._last_updated

    @property
    def from_date(self):
        return self._from_date

    @property
    def to_date(self):
        return self._to_date

    @property
    def routes(self):
        return self._routes

    def __repr__(self):
        return "<Disruption id:%r title:%r url:%r description:%r status:%r type:%r published_on:%r last_updated:%r from_date:%r to_date:%r routes:%r>" %(self.id, self.title, self.url, self.description, self.status, self.type, self.published_on, self.last_updated, self.from_date, self.to_date, self.routes)
