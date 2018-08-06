import urllib.request
import json
import pyptv3

class Client():
    """
    Create a client class that will get passed in to other API object"

    Args:
        developer_id (string): Your PTV API developer id
        api_key (string): Your PTV API api key
    Returns:
        client: The initialized client object. Pass this in to the API classes
    """
    def __init__(self, developer_id = None, api_key = None):
        self._url_builder = pyptv3.UrlBuilder(developer_id, api_key)

    def get(self, path, query_params = None):
        if query_params is None:
            query_params = []

        url = self._url_builder.build(path, query_params)

        try:
            response = urllib.request.urlopen(url)
            return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            self._handle_error(e)

    def _handle_error(self, error):
        if error.code == 400:
            raise pyptv3.InvalidRequestError(error.reason)
        elif error.code == 403:
            raise pyptv3.AccessDeniedError(error.reason)
        elif error.code == 404:
            raise pyptv3.NotFoundError(error.reason)
        else:
            raise pyptv3.UnknownError("Code: " + str(error.code) + " - " + error.reason)
