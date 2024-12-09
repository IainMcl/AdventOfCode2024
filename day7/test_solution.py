import pytest
from day7.solution import calibration, three_operator_calibration

@pytest.fixture
def input_data():
    return """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def testcalibration(input_data):
    assert calibration(input_data) == 3749

def test_three_operator_calibration(input_data):
    assert three_operator_calibration(input_data) == 11387
