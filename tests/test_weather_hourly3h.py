from seniverse import SeniverseV3
import pytest


@pytest.mark.skip('this api is premiums only')
def test_hourly3h(client: SeniverseV3):
    client.get_weather_hourly3h()
