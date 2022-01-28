from base64 import b64encode
import hashlib
import hmac
import json
import time
from typing import Literal
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


class SeniverseV4:
    def __init__(self, public_key, secret_key) -> None:
        self._endpoint = 'https://api.seniverse.com/v4'
        self._public_key = public_key
        self._secret_key = secret_key

    def fetch_data(self, fields: str, locations: str, **params):
        try:
            resp = urlopen(Request(self._signing(fields=fields, locations=locations, **params)))
        except HTTPError as err:
            print(err.read())
            raise
        data = json.load(resp)
        return data

    def _signing(self, **params):
        """ signing request

        :return: signed url
        :rtype: str
        """
        params['public_key'] = self._public_key
        params.setdefault('ts', str(int(time.time())))
        params.setdefault('ttl', '300')
        query = '&'.join('{}={}'.format(key, value) for key, value in sorted(params.items())).encode()
        params['sig'] = b64encode(hmac.new(self._secret_key.encode(), query, hashlib.sha1).digest()).decode()
        return self._endpoint+'?'+urlencode(params)

    def get_precipitation_minutely(self, locations: str):
        return self.fetch_data(fields='precip_minutely', locations=locations)
