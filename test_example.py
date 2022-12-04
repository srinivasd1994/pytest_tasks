# Example usage of the py.test fixture in tests
import socket
import pytest
import urllib

try:
    from urllib3 import urlopen
except ImportError:
    urlopen = urllib.request.urlopen


def test_socket_disabled_by_default():
    # default behavior: socket.socket is unusable
    with pytest.raises(RuntimeError):
        urlopen(u'https://www.python.org/')


def test_explicitly_enable_socket(enable_socket):
    # socket is enabled by pytest fixture from conftest. disabled in finalizer
    assert socket.socket(socket.AF_INET, socket.SOCK_STREAM)