from typing import List, Tuple, Optional, Final, Set, Dict
from pydantic import BaseModel
from itertools import combinations

class Maze(BaseModel):
    maze: List[List[str]]
    pos: Optional[Tuple[int, int]]
    direction: Optional[Tuple[int, int]] = None
    POSITION_MARKERS: Final = ["^", ">", "v", "<"] # in clockwise order
    DIRECTION_MAP: Final = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }
    BLOCKING_MARKERS: Final = ["#"]
    moves: int = 0
    visited_positions: Set[Tuple[int, int]] = set()
    path: List[Tuple[int, int]] = []

    def __init__(self, maze: List[List[str]], pos: Optional[Tuple[int, int]]):
        super().__init__(maze=maze, pos=pos)
        self.moves = 1
        # add starting position to visited positions
        if pos:
            self.visited_positions = {pos}
            self.path.append(pos)


    def find_position(self) -> Tuple[int, int]:
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                if cell in self.POSITION_MARKERS:
                    self.pos = (i, j)
                    self.direction = self.DIRECTION_MAP[cell]
                    return self.pos
        raise ValueError("Position not found")

    def move(self):
        if self.pos is None:
            return
        i, j = self.pos
        if not self.direction:
            raise ValueError("Direction not set")
        new_i, new_j = i + self.direction[0], j + self.direction[1]
        if new_i < 0 or new_i >= len(self.maze) or new_j < 0 or new_j >= len(self.maze[0]):
            # Out of bounds
            return
        if self.maze[new_i][new_j] in self.BLOCKING_MARKERS:
            # hit a wall turn right 
            self.turn_direction_right()
        else:
            self.pos = (new_i, new_j)
            # Add to visited positions
            prev_positions = len(self.visited_positions)
            self.visited_positions.add(self.pos)
            self.path.append(self.pos)
            if len(self.visited_positions) > prev_positions:
                # print( f"Adding {self.pos} to visited positions")
                pass
            else:
                # print(f"Already visited {self.pos}")
                pass
            self.moves += 1
        return True

    def turn_direction_right(self):
        if self.direction is None:
            raise ValueError("Direction not set")
        # apply rotation matrix to turn right
        self.direction = (self.direction[1], -self.direction[0])

    def __str__(self):
        return f"Maze(pos={self.pos}, direction={self.direction}, moves={self.moves})"

    def get_block_coords(self) -> List[Tuple[int, int]]:
        block_coords = []
        for i, row in enumerate(self.maze):
            for j, cell in enumerate(row):
                if cell in self.BLOCKING_MARKERS:
                    block_coords.append((i, j))
        return block_coords

    def find_possible_block_squares(self, block_coords: List[Tuple[int, int]]):
        """
        find squares that would result in a paradox if an obstacle was placed there
        This would be a position that would make a square with three other obstacles 
        The square would have a block at:
        top left + 1 in the y direction
        top right + 1 in the x direction
        bottom left - 1 in the x direction
        bottom right - 1 in the y direction
        """
        all_unique_three_obstacle_squares = list(combinations(block_coords, 3))
        # print(all_unique_three_obstacle_squares)
        square_completion_positions: Dict[int, Tuple[int, int]] = {}
        for i, square in enumerate(all_unique_three_obstacle_squares):
            p1, p2, p3 = square
            fourth_point = self.find_fourth_rectangle_point(p1, p2, p3)
            if self.in_maze(fourth_point) and self.is_on_path(fourth_point) and fourth_point not in block_coords:
                square_completion_positions[i] = fourth_point
        return square_completion_positions

    def is_on_path(self, point: Tuple[int, int]) -> bool:
        return point in self.visited_positions

    def in_maze(self, point: Tuple[int, int]) -> bool:
        i, j = point
        return i >= 0 and i < len(self.maze) and j >= 0 and j < len(self.maze[0])   

    @staticmethod
    def find_fourth_rectangle_point(p1, p2, p3):
        """
        Finds the fourth point to complete a rectangle given three points.
        Assumes the input points are tuples of (x, y).
        """
        # The fourth point is calculated by finding the missing vector that completes the parallelogram
        fourth_point = (
            p1[0] + p3[0] - p2[0],
            p1[1] + p3[1] - p2[1]
        )
        return fourth_point


    def find_paradox_obstacles(self) -> Set[Tuple[int, int]]:
        paradox_obstacles = []
        pass
        # for a paradox path a rectangle path needs to be made along the original path 
        # for this to happen there has to be an obstacle at
        # top left + 1 in the y direction 
        # top right + 1 in the x direction
        # bottom left - 1 in the x direction
        # bottom right - 1 in the y direction
        # One of these positions needs to be added as a paradox obstacle
        



def count_path(data:str) -> int:
    maze = parse_input(data)
    maze.find_position()
    moving = True 
    while moving:
        moving = maze.move()
    # print(maze.visited_positions)
    return len(maze.visited_positions)

def create_paradox(data:str) -> int:
    maze = parse_input(data)
    maze.find_position()
    moving = True
    while moving:
        moving = maze.move()
    # paradox_obstacle_positions = maze.find_paradox_obstacles()
    block_coords = maze.get_block_coords()
    points = maze.find_possible_block_squares(block_coords)
    print(points)
    # return len(paradox_obstacle_positions)
    return 0


def parse_input(data:str) -> Maze:
    maze = Maze(maze=[list(line) for line in data.split("\n")], pos=None)
    return maze

def main():
    with open("input.txt") as f:
        data = f.read()
    # print(count_path(data))
    print(create_paradox(data))

if __name__ == "__main__":
    main()
