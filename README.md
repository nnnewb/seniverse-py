# seniverse-py

![seniverse-py version badge](https://img.shields.io/pypi/v/seniverse-py?style=for-the-badge)
![seniverse-py python-version badge](https://img.shields.io/pypi/pyversions/seniverse-py?style=for-the-badge)
![seniverse-py license badge](https://img.shields.io/pypi/l/seniverse-py?style=for-the-badge)

seniverse-py is third-party sdk of seniverse.com (心知天气). only weather apis are implemented for now.

## CAUTION

Seniverse API v4 support still under development.

Because I don't have access to the Seniverse premium API and don't use the product in my work, development may be delayed or abandoned.

## Quickstart

install by `pip` command.

```shell
pip install seniverse-py
```

## Usage

```python
from seniverse import SeniverseV3
from os import getenv

api = SeniverseV3(getenv('SENIVERSE_UID'), getenv('SENIVERSE_KEY'))
resp = api.get_weather_now()
location = resp['results'][0]['location']
weather = resp['results'][0]['now']

print(f'今天{location["name"]}天气{weather["text"]}，气温{weather["temperature"]}°，更新于{weather["last_update"]}。')
```

## LICENSE

>                    GNU GENERAL PUBLIC LICENSE
>                       Version 3, 29 June 2007
>
> Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
> Everyone is permitted to copy and distribute verbatim copies
> of this license document, but changing it is not allowed.
