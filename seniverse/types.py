import sys
from typing import Any, Dict

# support typeddict
# https://www.python.org/dev/peps/pep-0589/
if sys.version_info.major == 3 and sys.version_info.minor >= 7:
    from typing import TypedDict

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

else:
    SignedUrlParams = Dict[str, Any]
    CommonParams = Dict[str, Any]
