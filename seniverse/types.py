try:
    from typing import TypedDict
except ImportError:
    # for python3.6+ compatible
    from typing_extensions import TypedDict

# support typeddict
# https://www.python.org/dev/peps/pep-0589/


class SignedUrlParams(TypedDict):
    """ ref: https://docs.seniverse.com/api/start/validation.html
    """
    ts: int
    ttl: int
    uid: str


class CommonParams(TypedDict):
    """ ref: https://docs.seniverse.com/api/start/common.html
    """
    location: str
    unit: str
    language: str
    scope: str
    start: int
    q: str
    port: str
    elements: str
    mask: str
