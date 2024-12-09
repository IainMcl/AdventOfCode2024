from typing import List, Dict, Callable 
from pydantic import BaseModel 
from itertools import combinations, product

class Eqn(BaseModel):
    sln: int
    inputs: List[int]

OPERATORS = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y
}

THREE_OPERATORS = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
    '||': lambda x, y: int(str(x) + str(y))
}

def can_evaluate(eqn: Eqn, operators_dict: Dict[str, Callable]) -> bool:
    # create all combinations of operators for each space available between numbers in the inputs 
    n_operators = len(eqn.inputs) - 1
    for operators in product(operators_dict.keys(), repeat=n_operators):
        # evaluate the equation with the current operators
        result = eqn.inputs[0]
        for i, operator in enumerate(operators):
            result = operators_dict[operator](result, eqn.inputs[i + 1])

        if result == eqn.sln:
            return True
    return False


def calibration(data: str) -> int:
    parsed_input = parse_input(data)
    total = 0
    for eqn in parsed_input:
        if can_evaluate(eqn, OPERATORS):
            total += eqn.sln
    return total

def three_operator_calibration(data: str) -> int:
    parsed_input = parse_input(data)
    total = 0
    for eqn in parsed_input:
        if can_evaluate(eqn, THREE_OPERATORS):
            total += eqn.sln
    return total

def parse_input(data: str) -> List[Eqn]:
    lines = data.strip().split("\n")
    # 190: 10 19 -> Eqn(sln=190, inputs=[10, 19])
    return [Eqn(sln=int(line.split(":")[0]), inputs=[int(x) for x in line.split(":")[1].split()]) for line in lines]

def main():
    with open("input.txt") as f:
        data = f.read()
    print(calibration(data))
    print(three_operator_calibration(data))

if __name__ == "__main__":
    main()
