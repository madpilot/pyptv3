import pyptv3

class Search:
    def __init__(self, client):
        self._client = client

    def term(self, term, **kwargs):
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/search/" + term, query_list)
