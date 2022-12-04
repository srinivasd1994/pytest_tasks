import pytest
ls_count = [(40, 10, 30), (60, 20, 40), (70, 30, 40), (50, 25, 25), ("are", "you", "going"), [1, 2, 6], {1, 2, 3}, {1:2, 3:4, 5:6}]
@pytest.mark.parametrize(('earned', 'spent', 'expected'), ls_count)
def test_transaction(earned, spent, expected):
    print(earned, spent, expected)