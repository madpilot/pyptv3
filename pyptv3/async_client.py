"""
    Provides an asyncio compatible Client.
"""
import json
import aiohttp
import pyptv3

def _handle_error(response):
    if response.status == 400:
        raise pyptv3.InvalidRequestError("Invalid Request")
    elif response.status == 403:
        raise pyptv3.AccessDeniedError("Access Denied")
    elif response.status == 404:
        raise pyptv3.NotFoundError("Not Found")
    else:
        raise pyptv3.UnknownError("Code: " + str(response.status) + " - unknown_error")

class AsyncClient(): # pylint: disable=too-few-public-methods
    """
    Create an async client class that will get passed in to other API object"

    Args:
        loop: Async IO loop object
        developer_id (string): Your PTV API developer id
        api_key (string): Your PTV API api key
    Returns:
        client: The initialized client object. Pass this in to the API classes
    """
    def __init__(self, loop, developer_id=None, api_key=None):
        self._loop = loop
        self._url_builder = pyptv3.UrlBuilder(developer_id, api_key)

    async def get(self, path, query_params=None):
        """
            Perform an API call

            Args:
                path (string): the path to GET
                query_params (list): List of query parameters to send
            Returns:
                An AsyncIO Coroutine
        """
        if query_params is None:
            query_params = []

        url = self._url_builder.build(path, query_params)

        async with aiohttp.ClientSession(loop=self._loop) as client:
            async with client.get(url) as response:
                if response.status == 200:
                    return json.loads(await response.read())
                _handle_error(response)
