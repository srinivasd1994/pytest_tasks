# def func(x):
#     return x + 1


# def test_answer():
#     assert func(3) == 5
# import pytest


# def f():
#     raise SystemExit()


# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()

class Class:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")