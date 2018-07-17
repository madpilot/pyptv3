import urllib.parse
import urllib.request
import hashlib
import hmac
import json
import pyptv3

class Client():
    API_BASE_URL = "https://timetableapi.ptv.vic.gov.au"
    VERSION = "v3"

    """
    Create a client class that will get passed in to other API object"

    Args:
        developer_id (string): Your PTV API developer id
        api_key (string): Your PTV API api key
    Returns:
        client: The initialized client object. Pass this in to the API classes
    """
    def __init__(self, developer_id = None, api_key = None):
        self._developer_id = developer_id
        self._api_key = api_key

    def get(self, path, query_params = []):
        url = self._build_url(path, query_params)

        try:
            response = urllib.request.urlopen(url)
            return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            self._handle_error(e)

    def _build_url(self, path, query_params):
        url = "/" + Client.VERSION + path

        parsed = urllib.parse.urlparse(url)
        query_params.append(("devid", self._developer_id))

        return Client.API_BASE_URL + self._sign(url, query_params)

    def _sign(self, url, query_params):
        pre_sign = url + "?" + urllib.parse.urlencode(query_params)

        digest = hmac.new(self._api_key.encode('utf-8'), pre_sign.encode('utf-8'), hashlib.sha1)
        signature = digest.hexdigest()

        query_params.append(("signature", signature.upper()))
        return url + "?" + urllib.parse.urlencode(query_params)

    def _handle_error(self, error):
        if error.code == 400:
            raise pyptv3.InvalidRequestError(error.reason)
        elif error.code == 403:
            raise pyptv3.AccessDeniedError(error.reason)
        elif error.code == 404:
            raise pyptv3.NotFoundError(error.reason)
        else:
            raise pyptv3.UnknownError("Code: " + str(error.code) + " - " + error.reason)
