from seniverse import SeniverseV3


def test_daily_forecast(client: SeniverseV3):
    client.get_weather_daily_forecast()
