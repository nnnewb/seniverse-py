from seniverse.client import SeniverseV3


def test_weather_now(client: SeniverseV3):
    data = client.get_weather_now()
    assert 'status' not in data
    assert 'status_code' not in data
