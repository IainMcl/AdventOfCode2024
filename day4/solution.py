from typing import List, Tuple

SIZE = 4
KEY = "XMAS"

directions = [
    (0, 1), # right
    (1, 0), # down
    (0, -1), # left
    (-1, 0), # up
    (-1, 1), # up_right
    (1, 1), # down_right
    (1, -1), # down_left
    (-1, -1) # up_left
]

def count_xmas(data: str) -> int:
    parsed_data = parse_input(data)
    count = 0
    for i, row in enumerate(parsed_data):
        for j, char in enumerate(row):
            if char == KEY[0]:
                for direction in directions:
                    if recursive_search(i, j, parsed_data, KEY, 0, direction):
                        count += 1
    return count

def recursive_search(i: int, j: int, arr: List[List[str]], word: str, word_position: int, direction: Tuple[int, int]) -> bool:
    if word_position == SIZE:
        return True
    if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[i]):
        # out of range
        return False
    # print(f"i: {i}, j: {j}, word_position: {word_position}, direction: {direction}, char: {arr[i][j]}, looking for: {word[word_position]}")
    if arr[i][j] != word[word_position]:
        return False
    return recursive_search(i+direction[0], j+direction[1], arr, word, word_position+1, direction)

def count_cross_mas(data: str) -> int:
    parsed_data = parse_input(data)
    count = 0
    search = "MS"
    rev_search = "SM"
    for i, row in enumerate(parsed_data):
        for j, char in enumerate(row):
            if char == "A":
                try:
                    if i == 0 or i == len(row)-1 or j == 0 or j == len(char)-1:
                        continue
                    top_left_to_bottom_right = parsed_data[i-1][j-1] + parsed_data[i+1][j+1]
                    top_right_to_bottom_left = parsed_data[i-1][j+1] + parsed_data[i+1][j-1]
                    if (top_left_to_bottom_right == search or top_left_to_bottom_right == rev_search) and (top_right_to_bottom_left == search or top_right_to_bottom_left == rev_search):
                        # print(f"i: {i}, j: {j}, top_left_to_bottom_right: {top_left_to_bottom_right}, top_right_to_bottom_left: {top_right_to_bottom_left}, search: {search}, rev_search: {rev_search}")
                        count += 1
                except IndexError:
                    continue
    return count

def find_key(i: int, j: int, arr: List[List[str]]) -> int:
    """
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]

    i = 2, j = 2

    [_, _, _,t, _],
    [_, _, _, _, _],
    [_, _, X, _, _],
    [_, _, _, _, _],
    [_, _, _, _, _]

    word = "XM"

    right = [i, j] -> [i, j+len(word)]
    down = [i, j] -> [i+len(word), j]
    left = [i, j] -> [i, j-len(word)]
    up = [i, j] -> [i-len(word), j]
    up_right = [i, j] -> [i-len(word), j+len(word)]
    down_right = [i, j] -> [i+len(word), j+len(word)]
    down_left = [i, j] -> [i+len(word), j-len(word)]
    up_left = [i, j] -> [i-len(word), j-len(word)]
    """ 
    word = "XMAS"
    count = 0
    # check right
    if j + len(word) < SIZE:
        if arr[i][j:j+len(word)] == word:
            print(arr[i][j:j+len(word)])
            count += 1
    # check down
    if i + len(word) < SIZE:
        if "".join([arr[i+k][j] for k in range(len(word))]) == word:
            count += 1
    # check left
    if j - len(word) >= 0:
        if arr[i][j-len(word):j] == word:
            count += 1
    # check up
    if i - len(word) >= 0:
        if "".join([arr[i-k][j] for k in range(len(word))]) == word:
            count += 1
    # check up_right
    if i - len(word) >= 0 and j + len(word) < SIZE:
        if "".join([arr[i-k][j+k] for k in range(len(word))]) == word:
            count += 1
    # check down_right
    if i + len(word) < SIZE and j + len(word) < SIZE:
        if "".join([arr[i+k][j+k] for k in range(len(word))]) == word:
            count += 1
    # check down_left
    if i + len(word) < SIZE and j - len(word) >= 0:
        if "".join([arr[i+k][j-k] for k in range(len(word))]) == word:
            count += 1
    # check up_left
    if i - len(word) >= 0 and j - len(word) >= 0:
        if "".join([arr[i-k][j-k] for k in range(len(word))]) == word:
            count += 1
    return count

def parse_input(data: str) -> List[List[str]]:
    parsed = [list(row) for row in data.split("\n")]
    return parsed


def main():
    with open("input.txt") as f:
        data = f.read()
    print(count_xmas(data))
    print(count_cross_mas(data))

if __name__ == "__main__":
    main()
