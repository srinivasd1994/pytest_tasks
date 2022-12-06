import pytest
import logging
@pytest.fixture(autouse=True)
def function_autouse():
    logging.info("scope function with autouse")
    
def test_autouse():
    assert True
    