import pytest
from day1.solution import get_total_distance, get_similarity

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

def test_get_total_distance_2(input_data):
    assert get_similarity(input_data) == 31
    


