from typing import List, Tuple
import re

from _pytest.capture import MultiCapture

def parse_and_solve(in_value: str) -> int:
    values = parse_input(in_value)
    sum = 0
    for pair in values:
        product = int(pair[0]) * int(pair[1])
        sum += product
    return sum

def parse_input(in_value: str) -> List[List[int]]:
    """
    Regex to parse a string looking for all strings like "mul(2,4)" 
    where each number can be up to 3 digits long
    """
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(regex, in_value)
    return matches

def parse_and_solve_do_dont(in_value: str) -> int:
    values = parse_input_do_dont(in_value)
    # join matches to one string then parse it
    mult_values = parse_input("".join(values))

    sum = 0
    for pair in mult_values:
        product = int(pair[0]) * int(pair[1])
        sum += product
    return sum

def parse_input_do_dont(in_value: str) -> str:
    """
    Regex to parse a string looking for all text between 'do()' and 'don't()' or the end of the line,
    and also from the start to the first 'don't()'
    """
    # pattern = r"/(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))/gm"
    pattern = r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
    matches = re.findall(pattern, in_value)
    new_matches = ""
    do = True
    for match in matches:
        # get the non null string from each tuple 
        for m in match:
            if m == "do()":
                do = True
            elif m == "don't()":
                do = False
            else:
                if m and do:
                    new_matches += m
    # flatten list of tuples
    return new_matches



def main():
    with open("input.txt") as f:
        data = f.read()
    print(parse_and_solve(data))
    print(parse_and_solve_do_dont(data))

if __name__ == "__main__":
    main()
