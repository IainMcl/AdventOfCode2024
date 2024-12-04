import pytest
from day2.solution import safe_reports_count, safe_reports_with_level_remove

@pytest.fixture
def input_data():
    return """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

def test_safe_reports_count(input_data):
    assert safe_reports_count(input_data) == 2

def test_safe_reports_with_level_remove(input_data):
    assert safe_reports_with_level_remove(input_data) == 4


