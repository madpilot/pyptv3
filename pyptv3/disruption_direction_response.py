""" Provides the DisruptionDirectionResponse Class """
import datetime

def _parse_time(time):
    return datetime.datetime.strptime(time, "%H:%M:%S")

class DisruptionDirectionResponse: # pylint: disable=line-too-long
    """
        Wraps the response from a Disruption request
    """
    def __init__(self, response):
        self._direction_id = response["direction_id"]
        self._name = response["direction_name"]
        self._route_direction_id = response["route_direction_id"]

        self._service_time = None
        if response["service_time"] is not None:
            self._service_time = _parse_time(response["service_time"])

    @property
    def direction_id(self):
        """
        Direction of travel identifier
        """
        return self._direction_id

    @property
    def name(self):
        """
        Name of direction of travel (str)
        """
        return self._name

    @property
    def route_direction_id(self):
        """
        Route and direction of travel combination identifierRoute and direction of travel combination identifierRoute and direction of travel combination identifier (int)
        """
        return self._route_direction_id


    @property
    def service_time(self):
        """
        Time of service to which disruption applies; returns null if disruption applies to multiple (or no) services (datetime)
        """
        return self._service_time

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<DisruptionDirection direction_id:%r name:%r route_direction_id:%r service_time:%r>" %(self.direction_id, self.name, self.route_direction_id, self.service_time)
