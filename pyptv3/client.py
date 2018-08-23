"""
    Provides the Client. A client instance gets passed to every pyptv3 class
    constructor.
"""

import urllib.request
import json
import pyptv3

def _handle_error(error):
    if error.code == 400:
        raise pyptv3.InvalidRequestError(error.reason)
    elif error.code == 403:
        raise pyptv3.AccessDeniedError(error.reason)
    elif error.code == 404:
        raise pyptv3.NotFoundError(error.reason)
    else:
        raise pyptv3.UnknownError("Code: " + str(error.code) + " - " + error.reason)

class Client(): # pylint: disable=too-few-public-methods
    """
        Create a client class that will get passed in to other API object"

        Args:
            developer_id (string): Your PTV API developer id
            api_key (string): Your PTV API api key
        Returns:
            client: The initialized client object. Pass this in to the API classes
    """
    def __init__(self, developer_id=None, api_key=None):
        self._url_builder = pyptv3.UrlBuilder(developer_id, api_key)

    def get(self, path, query_params=None):
        """
            Perform an API call

            Args:
                path (string): the path to GET
                query_params (list): List of query parameters to send
            Returns:
                None
        """
        if query_params is None:
            query_params = []

        url = self._url_builder.build(path, query_params)

        try:
            response = urllib.request.urlopen(url)
            return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as error:
            _handle_error(error)
