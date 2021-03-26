from os import getenv
from pytest import fixture
from seniverse.client import SeniverseV3


@fixture(scope='session')
def uid():
    uid = getenv('SENIVERSE_UID')
    assert uid is not None
    assert len(uid) > 0
    return uid


@fixture(scope='session')
def key():
    key = getenv('SENIVERSE_KEY')
    assert key is not None
    assert len(key) > 0
    return key


@fixture(scope='function')
def client(uid, key):
    from seniverse.client import SeniverseV3
    yield SeniverseV3(uid, key)
