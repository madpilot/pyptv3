"""
    Wraps Departure Responses
"""
import datetime

def _parse_datetime(time):
    return datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")

class DepartureResponse: # pylint: disable=too-many-instance-attributes
    """
        Service departures from the specified stop for the specified route (and route type);
        departures are timetabled and real-time (if applicable).
    """
    def __init__(self, response):
        self._stop_id = response["stop_id"]
        self._route_id = response["route_id"]
        self._run_id = response["run_id"]
        self._direction_id = response["direction_id"]
        self._disruption_ids = response["disruption_ids"]
        self._scheduled_departure = None

        if response["scheduled_departure_utc"]:
            self._scheduled_departure = _parse_datetime(response["scheduled_departure_utc"])

        self._estimated_departure = None
        if response["estimated_departure_utc"]:
            self._estimated_departure = _parse_datetime(response["estimated_departure_utc"])

        self._at_platform = response["at_platform"]
        self._platform_number = response["platform_number"]
        self._flags = response["flags"]
        self._sequence = response["departure_sequence"]

    @property
    def stop_id(self):
        """
            Stop identifier

            Returns:
                integer: The stop ID
        """
        return self._stop_id

    @property
    def route_id(self):
        """
            Route identifier

            Returns:
                integer: The route ID
        """
        return self._route_id

    @property
    def run_id(self):
        """
            Trip/service run identifier

            Returns:
                integer: The run ID
        """
        return self._run_id

    @property
    def direction_id(self):
        """
            Direction of travel identifier

            Returns:
                integer: The direction ID
        """
        return self._direction_id

    @property
    def disruption_ids(self):
        """
            Disruption information identifier(s)

            Returns:
                list: Disruption IDs
        """
        return self._disruption_ids

    @property
    def scheduled_departure(self):
        """
            Scheduled (i.e. timetabled) departure time and date in UTC

            Returns:
                datetime: The scheduled time
        """
        return self._scheduled_departure

    @property
    def estimated_departure(self):
        """
            Real-time estimate of departure time and date in UTC. Can be None

            Returns:
                datetime: The estimated time
        """
        return self._estimated_departure

    @property
    def at_platform(self):
        """
            Indicates if the metropolitan train service is at the platform at the time of query;
            returns false for other modes

            Returns:
                bool: True if the train is at the platform now
        """
        return self._at_platform

    @property
    def platform_number(self):
        """
            Platform number at stop
            (metropolitan train only; returns null for other modes)

            Returns:
                string: The platform numbers
        """
        return self._platform_number

    @property
    def flags(self):
        """
            Flag indicating special condition for run
            e.g. RR Reservations Required
                GC Guaranteed Connection
                DOO Drop Off Only
                PUO Pick Up Only
                MO Mondays only
                TU Tuesdays only
                WE Wednesdays only
                TH Thursdays only
                FR Fridays only
                SS School days only;
            ignore E flag

            Returns:
                string: The flags
        """
        return self._flags

    @property
    def sequence(self):
        """
            Chronological sequence of the departure for the run on the route.
            Order ascendingly by this field to get chronological order (earliest first)
            of departures with the same route_id and run_id.

            Returns:
                string: The flags
        """
        return self._sequence

    def __repr__(self):
        return """<Departure stop_id:%r
                            route_id:%r
                            run_id:%r
                            direction_id:%r
                            disruption_ids: %r
                            scheduled_departure:%r
                            estimated_departure:%r
                            at_platform:%r
                            platform_number:%r
                            flags:%r sequence:%r>""" % (\
                                self.stop_id,
                                self.route_id,
                                self.run_id,
                                self.direction_id,
                                self._disruption_ids,
                                self.scheduled_departure,
                                self.estimated_departure,
                                self.at_platform,
                                self.platform_number,
                                self.flags,
                                self.sequence)
