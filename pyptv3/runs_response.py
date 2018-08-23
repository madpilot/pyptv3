import pyptv3

class RunsResponse:
    def __init__(self, response):
        self._runs = list(map(lambda t: pyptv3.RunResponse(t), response["runs"]))
        self._status = pyptv3.StatusResponse(response["status"])

    @property
    def runs(self):
        return self._runs

    @property
    def status(self):
        return self._status

    def __repr__(self):
        return "<Runs runs:%r status:%r>" %(self.runs, self.status)

    def __getitem__(self, key):
        return self.runs[key]

    def __iter__(self):
        return self.runs.__iter__()

    def __len__(self):
        return self.runs.__len__()
