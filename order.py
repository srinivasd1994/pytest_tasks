import unittest
import pytest

class Test2(unittest.TestCase):

    @pytest.mark.run(order=4)
    def testa(self):
        pass

    @pytest.mark.run(order=3)
    def testb(self):
        pass

    @pytest.mark.run(order=2)
    def testc(self):
        pass

    @pytest.mark.run(order=1)
    def testd(self):
        pass