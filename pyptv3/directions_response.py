""" Provides the DirectionsResponse Class """
import pyptv3

class DirectionsResponse(): # pylint: disable=unnecessary-lambda
    """
        Wraps the response from a Directions request
    """
    def __init__(self, response):
        self._directions = list(map(lambda t: \
            pyptv3.DirectionResponse(t), response["directions"]))

        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def directions(self):
        """
        Directions of travel of route

        Returns:
            list: of pyptv3.Direction
        """
        return self._directions

    @property
    def status(self):
        """
        API Status object

        Returns:
            pyptv3.Status
        """
        return self._status

    def __repr__(self):
        return "<Directions directions:%r status:%r>" %(self.directions, self.status)

    def __getitem__(self, key):
        return self.directions[key]

    def __iter__(self):
        return self.directions.__iter__()

    def __len__(self):
        return self.directions.__len__()
