import pytest
from solution import get_total_diatance

@pytest.fixture
def input_data():
    return """3   4
4   3
2   5
1   3
3   9
3   3
    """

def test_get_total_distance(input_data):
    assert get_total_distance(input_data) == 11
    


