import pytest
import requests
import _socket_toggle

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())

@pytest.fixture
def supply_url():
    return "https://reqres.in/api/users"


def pytest_runtest_setup():
    """ disable the interet. test-cases can explicitly re-enable """
    _socket_toggle.disable_socket()


@pytest.fixture(scope='function')
def enable_socket(request):
    """ re-enable socket.socket for duration of this test function """
    _socket_toggle.enable_socket()
    request.addfinalizer(_socket_toggle.disable_socket)