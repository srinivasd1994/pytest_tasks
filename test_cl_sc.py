import pytest
import db
# import logging
# @pytest.fixture(scope="class")
# def dummy_data(request):
#     request.cls.num1 = 10
#     request.cls.num2 = 20
#     logging.info("Execute fixture")

# @pytest.mark.usefixtures("dummy_data")
# class TestCalculatorClass:
#     def test_distance(self):
#         logging.info("Test distance function")
#         assert distance(self.num1, self.num2) == 10

#     def test_sum_of_square(self):
#         logging.info("Test sum of square function")
#         assert sum_of_square(self.num1, self.num2) == 500


# def distance(num1, num2):
#     return abs(num1 - num2)

# def sum_of_square(num1, num2):
#     return num1 ** 2 + num2 ** 2

@pytest.fixture(scope="class")
def prepare_db(request):
    # pseudo code
    connection = db.create_connection()
    request.cls.connection = connection
    yield
    connection = db.close()

@pytest.mark.usefixtures("prepare_db")
class TestDBClass:
    def test_query1(self):
        assert self.connection.execute("..") == "..."

    def test_query2(self):
        assert self.connection.execute("..") == "..."