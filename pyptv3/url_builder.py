import urllib.parse
import hashlib
import hmac

class UrlBuilder():
    API_BASE_URL = "https://timetableapi.ptv.vic.gov.au"
    VERSION = "v3"

    def __init__(self, developer_id = None, api_key = None):
        self._developer_id = developer_id
        self._api_key = api_key

    def build(self, path, query_params):
        url = "/" + UrlBuilder.VERSION + path

        parsed = urllib.parse.urlparse(url)
        query_params.append(("devid", self._developer_id))

        return UrlBuilder.API_BASE_URL + self._sign(url, query_params)

    def _sign(self, url, query_params):
        pre_sign = url + "?" + urllib.parse.urlencode(query_params)

        digest = hmac.new(self._api_key.encode('utf-8'), pre_sign.encode('utf-8'), hashlib.sha1)
        signature = digest.hexdigest()

        query_params.append(("signature", signature.upper()))
        return url + "?" + urllib.parse.urlencode(query_params)
