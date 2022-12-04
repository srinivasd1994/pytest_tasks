import pytest

@pytest.mark.smoke # user define marker
def test_pro():
    pass
@pytest.mark.resp
def test_apro():
    pass
@pytest.mark.smoke
def test_smpro():
    pass
@pytest.mark.resp
def test_upro():
    pass

    