from seniverse import SeniverseV3
import pytest


@pytest.mark.skip('this api is premiums only')
def test_weather_pricipitation_forecast(client: SeniverseV3):
    client.get_weather_precipitation_forecast()
