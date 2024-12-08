import pytest
from day6.solution import count_path, create_paradox

@pytest.fixture
def input_data():
    return """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

def test_count_path(input_data):
    assert count_path(input_data) == 41

def test_create_paradox(input_data):
    assert create_paradox(input_data) == 6

