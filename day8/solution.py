from typing import List, Dict, Callable , Tuple
from pydantic import BaseModel 
from itertools import combinations, product

Grid = List[List[str]]
Point = Tuple[int, int]

def get_same_frequencies(grid: Grid) -> Dict[str, List[Point]]:
    freq_map = {}
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell in freq_map and is_node(cell):
                freq_map[cell].append((i, j))
            else:
                freq_map[cell] = [(i, j)]
    return freq_map

def is_node(cell: str) -> bool:
    if cell.isalpha() or cell.isdigit():
        return True
    return False

def get_anti_nodes(a: Point, b: Point) -> List[Point]:
    vector_between = (b[0] - a[0], b[1] - a[1])
    return [(a[0] - vector_between[0], a[1] - vector_between[1]),
            (b[0] + vector_between[0], b[1] + vector_between[1])]

def get_t_anti_nodes(a: Point, b: Point, grid: Grid) -> List[Point]:
    # this includes the other point as a node as well so the new nodes would be nodes - 2 
    # but here we want to include the nodes as well so this includes them
    vector_between = (b[0] - a[0], b[1] - a[1])
    nodes = []
    cur_node = a
    while is_in_grid(cur_node, grid):
        nodes.append(cur_node)
        cur_node = (cur_node[0] + vector_between[0], cur_node[1] + vector_between[1])
    cur_node = a
    while is_in_grid(cur_node, grid):
        nodes.append(cur_node)
        cur_node = (cur_node[0] - vector_between[0], cur_node[1] - vector_between[1])
    return nodes


def is_in_grid(a: Point, grid: Grid) -> bool:
    return 0 <= a[0] < len(grid) and 0 <= a[1] < len(grid[0])

def get_node_pairs(nodes: List[Point]) -> List[Tuple[Point, Point]]:
    return list(combinations(nodes, 2))

def a_frequency(data: str) -> int:
    input_data = parse_input(data)
    freq_map = get_same_frequencies(input_data)
    unique_anti_nodes = set()
    for freq in freq_map:
        if len(freq_map[freq]) > 1:
            node_pairs = get_node_pairs(freq_map[freq])
            for node_pair in node_pairs:
                anti_nodes = get_anti_nodes(*node_pair)
                for anti_node in anti_nodes:
                    if is_in_grid(anti_node, input_data):
                        unique_anti_nodes.add(anti_node)
    return len(unique_anti_nodes)

def t_frequency(data: str) -> int:
    input_data = parse_input(data)
    freq_map = get_same_frequencies(input_data)
    unique_anti_nodes = set()
    for freq in freq_map:
        if len(freq_map[freq]) > 1:
            node_pairs = get_node_pairs(freq_map[freq])
            for node_pair in node_pairs:
                anti_nodes = get_t_anti_nodes(*node_pair, input_data)
                for anti_node in anti_nodes:
                    unique_anti_nodes.add(anti_node)
    return len(unique_anti_nodes)

def parse_input(data: str) -> List[List[str]]:
    lines = data.strip().split("\n")
    return [list(line) for line in lines]

def main():
    with open("input.txt") as f:
        data = f.read()
    print(a_frequency(data))
    print(t_frequency(data))

if __name__ == "__main__":
    main()
