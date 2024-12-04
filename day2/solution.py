# from typing import List, Tuple
# 
# def safe_reports_count(in_value:str)-> int:
#     data = parse_input(in_value)
#     count = 0
#     for row in data:
#         if is_safe(row)[0]:
#             # print(row)
#             count += 1
# 
#     return count
# 
# def is_safe(row: List[int]) -> Tuple[bool, int]:
#     """
#     Safe if all values are either increasing or decreasing with each step being 
#     less than or equal to 3 in difference
#     Returns bool and if false then the problem index
#     """
#     decreasing = True if row[0] > row[1] else False
#     for i in range(len(row) - 1):
#         diff = abs(row[i] - row[i+1])
#         if diff > 3 or diff == 0:
#             return False, i
#         if row[i] < row[i+1] and decreasing or row[i] > row[i+1] and not decreasing:
#             return False, i
#     return True, -1
# 
# def safe_reports_with_level_remove(in_value:str)-> int:
#     data = parse_input(in_value)
#     count = 0
#     for row in data:
#         safe, idx = is_safe(row)
#         if safe:
#             count += 1
#         else:
#             if is_safe_with_level_remove(row, idx):
#                 count += 1
#     return count
# 
# def is_safe_with_level_remove(row: List[int], index: int) -> bool:
#     """Remove the problem index from the row and check if it is safe now"""
#     row.pop(index)
#     safe, idx = is_safe(row)
#     if not safe:
#         if len(set(row)) != len(row) or max(row) - min(row) > 3 * len(row):
#             # Check if all values are increasing or decreasing
#             if all(row[i] < row[i+1] for i in range(len(row) - 1)) or all(row[i] > row[i+1] for i in range(len(row) - 1)):
#                 pass
#                 # print(row, idx)
#     return safe
# 
# def parse_input(in_value: str) -> List[List[int]]:
#     row = in_value.strip().split("\n")
#     values = [row.split(" ") for row in row]
#     inv_values = [[int(x) for x in row] for row in values]
#     return inv_values
# 
# def main():
#     with open("input.txt") as f:
#         data = f.read()
#     print(safe_reports_count(data))
#     print(safe_reports_with_level_remove(data))
# 
# if __name__ == "__main__":
#     main()
# 
from typing import List, Tuple

def safe_reports_count(in_value: str) -> int:
    data = parse_input(in_value)
    count = 0
    for row in data:
        if is_safe(row)[0]:
            count += 1
    return count

def is_safe(row: List[int]) -> Tuple[bool, int]:
    """
    Safe if all values are either increasing or decreasing with each step being 
    less than or equal to 3 in difference
    Returns bool and if false then the problem index
    """
    decreasing = True if row[0] > row[1] else False
    for i in range(len(row) - 1):
        diff = abs(row[i] - row[i+1])
        if diff > 3 or diff == 0:
            return False, i
        if row[i] < row[i+1] and decreasing or row[i] > row[i+1] and not decreasing:
            return False, i
    return True, -1

def safe_reports_with_level_remove(in_value: str) -> int:
    data = parse_input(in_value)
    count = 0
    for row in data:
        safe, idx = is_safe(row)
        if safe:
            count += 1
        else:
            if is_safe_with_level_remove(row):
                count += 1
    return count

def is_safe_with_level_remove(row: List[int]) -> bool:
    """Remove each element one by one and check if the row is safe"""
    for i in range(len(row)):
        new_row = row[:i] + row[i+1:]
        if is_safe(new_row)[0]:
            return True
    return False

def parse_input(in_value: str) -> List[List[int]]:
    rows = in_value.strip().split("\n")
    values = [row.split(" ") for row in rows]
    inv_values = [[int(x) for x in row] for row in values]
    return inv_values

def main():
    with open("input.txt") as f:
        data = f.read()
    print("Safe reports count:", safe_reports_count(data))
    print("Safe reports with level remove count:", safe_reports_with_level_remove(data))

if __name__ == "__main__":
    main()
