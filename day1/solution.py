from typing import List

def get_total_distance(in_value: str) -> int:
    data = parse_input(in_value)
    for l in data:
        l.sort()

    total = 0
    for val in zip(*data):
        total += abs(val[0] - val[1])
    return total

def get_similarity(in_value: str) -> int:
    data = parse_input(in_value)
    similarity = 0
    for val in data[0]:
        count = 0
        for val2 in data[1]:
            if val == val2:
                count += 1
        similarity += count * val
    return similarity

def parse_input(in_value: str) -> List[List[int]]:
    """
    Parse string input two colums of integers separated by 3x spaces
    each column is one list of numers.
    Return the two lists as a list
    """
    rows = in_value.strip().split("\n")
    values = [row.split("   ") for row in rows]
    inv_values = [[int(x) for x in row] for row in values]
    list1, list2 = zip(*inv_values)
    return [list(list1), list(list2)]

def main():
    with open("input.txt") as f:
        data = f.read()
    print(get_total_distance(data))
    print(get_similarity(data))
    

if __name__ == "__main__":
    main()
