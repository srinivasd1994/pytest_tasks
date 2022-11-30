# def aree():
#     return 6 + 5

# def test_ar(aree):
#     assert aree == 11
import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1