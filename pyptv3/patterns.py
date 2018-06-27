import pyptv3

class Patterns:
    def __init__(self, client, run_id, route_type):
        self._client = client
        self._run_id = run_id
        self._route_type = route_type

    def all(self, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/pattern/run/" + str(self._run_id) + "/route_type/" + str(self._route_type), query_list)
