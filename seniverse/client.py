from seniverse.exceptions import SeniverseV3ApiError
from typing import Any, Dict, Literal
import requests

from seniverse.types import CommonParams


class SeniverseV3:

    def __init__(self, uid: str, key: str, *, use_https: bool = True):
        self._key = key
        self._uid = uid
        self._use_https = use_https

    @property
    def schema(self):
        if self._use_https:
            return 'https'
        else:
            return 'http'

    @property
    def base_url(self):
        return f'{self.schema}://api.seniverse.com/v3'

    @property
    def uid(self):
        return self._uid

    def _get(self, url: str, params: CommonParams) -> Dict[str, Any]:
        params['key'] = self._key
        data = requests.get(url, params=params).json()
        if data.get('status_code'):
            raise SeniverseV3ApiError(data['status_code'], data['status'])

        return data

    def get_weather_now(self, location: str = 'ip', language: str = 'zh-Hans', unit: Literal['c', 'f'] = 'c'):
        """实况天气

        ref: https://docs.seniverse.com/api/weather/now.html

        :param location: 地点, defaults to 'ip'
        :type location: str, optional
        :param language: 语言, defaults to 'zh-hans'
        :type language: str, optional
        :param unit: 单位, defaults to 'c'，可选 'f'
        :type unit: str, optional
        """
        return self._get(f'{self.base_url}/weather/now.json', {
            'location': location,
            'language': language,
            'unit': unit,
        })

    def get_weather_precipitation_forecast(self, location: str = 'ip'):
        """分钟级降水预报

        ref: https://docs.seniverse.com/api/weather/minutely.html

        :param location: 地点, defaults to 'ip'
        :type location: str, optional
        """
        return self._get(f'{self.base_url}/weather/grid/minutely.json', {'location': location})

    def get_weather_daily_forecast(self, location: str = 'ip', language: str = 'zh-Hans', unit: Literal['c', 'f'] = 'c', start: int = 0, days: int = 3):
        """逐日天气预报

        :param location: 地点, defaults to 'ip'
        :type location: str, optional
        :param language: 语言, defaults to 'zh-Hans'
        :type language: str, optional
        :param unit: 单位, defaults to 'c'
        :type unit: Literal[, optional
        :param start: 开始日期，0表示今天, defaults to 0
        :type start: int, optional
        :param days: 预报天数, defaults to 3
        :type days: int, optional
        """
        return self._get(f'{self.base_url}/weather/daily.json', {
            'location': location,
            'language': language,
            'unit': unit,
            'start': start,
            'days': days,
        })

    def get_weather_hourly_forecast(self, location: str = 'ip', language: str = 'zh-Hans', unit: Literal['c', 'f'] = 'c', start: int = 0, hours: int = 0):
        return self._get(f'{self.base_url}/weather/hourly.json', {
            'location': location,
            'language': language,
            'unit': unit,
            'start': start,
            'hours': hours,
        })

    def get_weather_hourly_history(self, location: str = 'ip', language: str = 'zh-Hans', unit: Literal['c', 'f'] = 'c'):
        return self._get(f'{self.base_url}/weather/hourly_history.json', {
            'location': location,
            'language': language,
            'unit': unit,
        })

    def get_weather_hourly3h(self, location: str = 'ip', unit: Literal['c', 'f'] = 'c'):
        return self._get(f'{self.base_url}/weather/hourly3h.json', {
            'location': location,
            'unit': unit,
        })

    def get_weather_alarm(self, location: str = 'ip'):
        return self._get(f'{self.base_url}/weather/alarm.json', {'location': location, })
