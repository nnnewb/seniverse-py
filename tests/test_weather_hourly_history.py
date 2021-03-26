import pytest
from seniverse import SeniverseV3


@pytest.mark.skip('this api is premiums only')
def test_hourly_history(client: SeniverseV3):
    client.get_weather_hourly_history()
