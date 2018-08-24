""" Provides the DisruptionsResponse Class """
import pyptv3

class DisruptionsResponse(): # pylint: disable=line-too-long,unnecessary-lambda
    """
        Wraps the response from a Disruptions request
    """
    def __init__(self, response):
        self._disruptions = {}
        self._disruptions["general"] = []
        self._disruptions["metro_train"] = []
        self._disruptions["metro_tram"] = []
        self._disruptions["metro_bus"] = []
        self._disruptions["regional_train"] = []
        self._disruptions["regional_coach"] = []
        self._disruptions["regional_bus"] = []

        if response["disruptions"]["general"] is not None:
            self._disruptions["general"] = list(map(lambda t: pyptv3.DisruptionResponse(t), response["disruptions"]["general"]))

        if response["disruptions"]["metro_train"] is not None:
            self._disruptions["metro_train"] = list(map(lambda t: pyptv3.DisruptionResponse(t), response["disruptions"]["metro_train"]))

        if response["disruptions"]["metro_tram"] is not None:
            self._disruptions["metro_tram"] = list(map(lambda t: pyptv3.DisruptionResponse(t), response["disruptions"]["metro_tram"]))

        if response["disruptions"]["metro_bus"] is not None:
            self._disruptions["metro_bus"] = list(map(lambda t: pyptv3.DisruptionResponse(t), response["disruptions"]["metro_bus"]))

        if response["disruptions"]["regional_train"] is not None:
            self._disruptions["regional_train"] = list(map(lambda t: pyptv3.DisruptionResponse(t), response["disruptions"]["regional_train"]))

        if response["disruptions"]["regional_coach"] is not None:
            self._disruptions["regional_coach"] = list(map(lambda t: pyptv3.DisruptionResponse(t), response["disruptions"]["regional_coach"]))

        if response["disruptions"]["regional_bus"] is not None:
            self._disruptions["regional_bus"] = list(map(lambda t: pyptv3.DisruptionResponse(t), response["disruptions"]["regional_bus"]))

        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def disruptions(self):
        """
        Disruption information applicable to relevant routes or stops
        """
        return self._disruptions

    @property
    def status(self):
        """
        API Status object

        Returns:
            pyptv3.Status
        """
        return self._status

    def __repr__(self):
        return "<Disruptions disruptions:%r status:%r>" %(self.disruptions, self.status)

    def __getitem__(self, key):
        return self.disruptions[key]

    def __iter__(self):
        return self.disruptions.__iter__()

    def __len__(self):
        return self.disruptions.__len__()
