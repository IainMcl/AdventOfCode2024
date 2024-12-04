import pytest
from day3.solution import parse_and_solve, parse_and_solve_do_dont

@pytest.fixture
def input_data():
    return """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))mul(12345,4))"""

def test_safe_reports_count(input_data):
    assert parse_and_solve(input_data) == 161

@pytest.fixture
def do_dont_input_data():
    return """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

def test_safe_reports_count_do_dont(do_dont_input_data):
    assert parse_and_solve_do_dont(do_dont_input_data) == 48
