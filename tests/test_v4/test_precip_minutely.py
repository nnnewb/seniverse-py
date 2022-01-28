from seniverse import SeniverseV4


def test_precip_minutely(client_v4: SeniverseV4):
    data = client_v4.get_precipitation_minutely('116.403635:39.919572')
    assert 'status' not in data
    assert 'status_code' not in data
