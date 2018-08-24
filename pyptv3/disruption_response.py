""" Provides the DisruptionResponse Class """
import pyptv3
import datetime

def _parse_datetime(date_time):
    return datetime.datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%SZ")

class DisruptionResponse: # pylint: disable=line-too-long
    """
        Wraps the response from a Disruption request
    """
    def __init__(self, response):
        self._disruption_id = response["disruption_id"]
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
            self._published_on = _parse_datetime(response["published_on"])

        if response["last_updated"] is not None:
            self._last_updated = _parse_datetime(response["last_updated"])

        if response["from_date"] is not None:
            self._from_date = _parse_datetime(response["from_date"])

        if response["to_date"] is not None:
            self._to_date = _parse_datetime(response["to_date"])

        self._routes = []
        if response["routes"] is not None:
            self._routes = list(map(lambda t: pyptv3.DisruptionRouteResponse(t), response["routes"]))

    @property
    def disruption_id(self):
        """
        Disruption information identifier (int)
        """
        return self._disruption_id

    @property
    def title(self):
        """
        Headline title summarising disruption information (str)
        """
        return self._title

    @property
    def url(self):
        """
        URL of relevant article on PTV website (str)
        """
        return self._url

    @property
    def description(self):
        """
        Description of the disruption (str)
        """
        return self._description

    @property
    def status(self):
        """
        Status of the disruption (e.g. "Planned", "Current")  (str)
        """
        return self._status

    @property
    def type(self):
        """
        Type of disruption (str)
        """
        return self._type

    @property
    def published_on(self):
        """
        Date and time disruption information is published on PTV website, (datetime)
        """
        return self._published_on

    @property
    def last_updated(self):
        """
        Date and time disruption information was last updated by PTV (datetime)
        """
        return self._last_updated

    @property
    def from_date(self):
        """
        Date and time at which disruption begins (datetime)
        """
        return self._from_date

    @property
    def to_date(self):
        """
        Date and time at which disruption ends (datetime)
        """
        return self._to_date

    @property
    def routes(self):
        """
        Route relevant to a disruption (list [pyptv3.DistruptionRouteResponse]
        """
        return self._routes

    def __repr__(self):
        return "<Disruption disruption_id:%r title:%r url:%r description:%r status:%r type:%r published_on:%r last_updated:%r from_date:%r to_date:%r routes:%r>" %(self.disruption_id, self.title, self.url, self.description, self.status, self.type, self.published_on, self.last_updated, self.from_date, self.to_date, self.routes)
