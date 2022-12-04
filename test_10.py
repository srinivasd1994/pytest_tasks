import pytest

def test_hakun():
    pass

@pytest.mark.xfail
def test_hak():
    assert True

@pytest.mark.xfail
def test_hak1():
    assert False