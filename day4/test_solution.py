import pytest
from day4.solution import count_xmas, count_cross_mas

@pytest.fixture
def input_data():
    return """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

@pytest.fixture 
def short_input_data():
    return """XMAS
XMAS"""

def test_count_xmas(input_data):
    assert count_xmas(input_data) == 18

def test_cross_mass(input_data):
    assert count_cross_mas(input_data) == 9
