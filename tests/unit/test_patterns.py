import pytest
from mock import Mock
from pyptv3 import Patterns

class TestPatterns:
    @pytest.fixture(scope="module")
    def client(self):
        return Mock()

    def test_all(self, client):
        Patterns(client, 1, 0).all()
        client.get.assert_called_with("/pattern/run/1/route_type/0", [])

    def test_all_with_kwargs(self, client):
        Patterns(client, 1, 0).all(expand=["stop", "route"], stop_id=10, date_utc="2018-06-28T07:00:00Z")
        client.get.assert_called_with("/pattern/run/1/route_type/0", [("expand", "stop"), ("expand", "route"), ("stop_id", 10), ("date_utc", "2018-06-28T07:00:00Z")])
