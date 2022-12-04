from __future__ import print_function
import socket
import sys

_module = sys.modules[__name__]

def disable_socket():
    """ disable socket.socket to disable the Internet. useful in testing.

    .. doctest::
        >>> enable_socket()
        [!] socket.socket is enabled.
        >>> disable_socket()
        [!] socket.socket is disabled. Welcome to the desert of the real.
        >>> socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Traceback (most recent call last):
        ...
        RuntimeError: I told you not to use the Internet!
        >>> enable_socket()
        [!] socket.socket is enabled.
        >>> enable_socket()
        [!] socket.socket is enabled.
        >>> disable_socket()
        [!] socket.socket is disabled. Welcome to the desert of the real.
        >>> socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Traceback (most recent call last):
        ...
        RuntimeError: I told you not to use the Internet!
        >>> enable_socket()
        [!] socket.socket is enabled.
    """
    setattr(_module, '_socket_disabled', True)

    def guarded(*args, **kwargs):
        if getattr(_module, '_socket_disabled', False):
            raise RuntimeError("I told you not to use the Internet!")
        else:
            # SocketType is a valid public alias of socket.socket,
            # we use it here to avoid namespace collisions
            return socket.SocketType(*args, **kwargs)

    socket.socket = guarded

    print(u'[!] socket.socket is disabled. Welcome to the desert of the real.')


def enable_socket():
    """ re-enable socket.socket to enable the Internet. useful in testing.
    """
    setattr(_module, '_socket_disabled', False)
    print(u'[!] socket.socket is enabled.')