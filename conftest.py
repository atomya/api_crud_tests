import pytest
import inspect
import logging

import requests

logger = logging.getLogger("example." + __name__)


class RestfulClient:

    _s = requests.session()
    host = None

    def __init__(self, host):
        self.host = host

    def verify_response(
            self, res: requests.Response, ok_status=200
    ) -> requests.Response:
        func = inspect.stack()[1][3]
        if isinstance(ok_status, int):
            ok_status = [ok_status]
        if res.status_code not in ok_status:
            raise ValueError(
                f"Verified response: function {func} failed: "
                f"server responded {res.status_code} "
                f"with data: {res.content}"
            )
        else:
            logger.info(
                f"Verified response: function {func} code {res.status_code}"
            )
        return res

    vr = verify_response



    def create_user(self, data: dict):
        return self._s.post(self.host + "/users/", json=data)

    def update_user(self, uid: int,  data: dict):
        return self._s.patch(self.host + f"/users/{uid}", json=data)

    def get_user(self, uid: int):
        return self._s.get(self.host + f"/users/{uid}")

    def delete_user(self, uid: int):
        return self._s.delete(self.host + f"/users/{uid}")


@pytest.fixture(scope="session")
def client():
    client = RestfulClient("http://localhost:8080/api")
    return client