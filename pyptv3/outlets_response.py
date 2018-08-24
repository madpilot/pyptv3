""" Provides the OutletsResponse Class """
import pyptv3

class OutletsResponse(): # pylint: disable=unnecessary-lambda
    """
        Wraps the response from a Outlets request
    """
    def __init__(self, response):
        self._outlets = list(map(lambda t: pyptv3.OutletResponse(t), response["outlets"]))
        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def outlets(self):
        """
        myki ticket outlets
        """
        return self._outlets

    @property
    def status(self):
        """
        API Status object

        Returns:
            pyptv3.Status
        """
        return self._status

    def __repr__(self):
        return "<Outlets outlets:%r status:%r>" %(self.outlets, self.status)

    def __getitem__(self, key):
        return self.outlets[key]

    def __iter__(self):
        return self.outlets.__iter__()

    def __len__(self):
        return self.outlets.__len__()
