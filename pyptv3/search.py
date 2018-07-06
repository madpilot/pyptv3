import pyptv3
import urllib.parse

class Search:
    def __init__(self, client):
        self._client = client

    def term(self, term, **kwargs):
        quoted = urllib.parse.quote(term)
        query_list = pyptv3.QueryParams.process_kwargs(**kwargs)
        return self._client.get("/search/" + quoted, query_list)
