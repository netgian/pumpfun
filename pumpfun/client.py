import requests
from .config import *


class Client:
    def __init__(self, base_url, headers, timeout):
        self.base_url = base_url
        self.headers = headers
        self.timeout = timeout

    def request(self, method: str, endpoint: str, params: dict=None, data: dict=None, json: dict=None) -> [dict, str]:
        try:
            r = requests.request(
                method=method,
                url=self.base_url + endpoint,
                params=params,
                data=data,
                json=json,
                headers=self.headers,
                timeout=self.timeout
            )
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request failed: {e}")

        try:
            return r.json()
        except ValueError:
            return r.text


client = Client(base_url=BASE_URL, headers=DEFAULT_HEADERS, timeout=DEFAULT_TIMEOUT)
