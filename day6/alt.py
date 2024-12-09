from collections import deque

def parse_input(input_map):
    grid = [list(row) for row in input_map.splitlines()]
    rows, cols = len(grid), len(grid[0])
    guard_pos = None
    direction = None

    # Find the guard's starting position and direction
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                direction = directions[grid[r][c]]
                grid[r][c] = '.'  # Replace the guard symbol with empty space
                break
        if guard_pos:
            break

    return grid, guard_pos, direction

def is_valid_pos(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '.'

def simulate_guard(grid, start_pos, start_dir):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Up, Right, Down, Left
    dir_index = directions.index(start_dir)
    visited = set()
    path = []
    pos = start_pos

    while pos not in visited:
        visited.add(pos)
        path.append(pos)
        r, c = pos
        dr, dc = directions[dir_index]
        # Check if the next position is valid
        if is_valid_pos(grid, r + dr, c + dc):
            pos = (r + dr, c + dc)
        else:
            dir_index = (dir_index + 1) % 4  # Turn right

    return path

def find_loop_positions(grid, guard_pos, guard_dir):
    path = simulate_guard(grid, guard_pos, guard_dir)
    loop_positions = set()
    for obstruction_pos in path:
        test_grid = [row[:] for row in grid]
        r, c = obstruction_pos
        test_grid[r][c] = '#'
        simulated_path = simulate_guard(test_grid, guard_pos, guard_dir)
        if len(simulated_path) < len(path):  # Guard got stuck in a loop
            loop_positions.add(obstruction_pos)
            print(f"Obstacle position {obstruction_pos} caused a loop")
    return loop_positions

def main(input_map):
    grid, guard_pos, guard_dir = parse_input(input_map)
    loop_positions = find_loop_positions(grid, guard_pos, guard_dir)
    print(loop_positions)
    return len(loop_positions)

# Example input
input_map = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

# Run the solution
print(main(input_map))
