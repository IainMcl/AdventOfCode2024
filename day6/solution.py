from typing import List, Tuple, Optional, Final, Set
from pydantic import BaseModel

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
                print( f"Adding {self.pos} to visited positions")
            else:
                print(f"Already visited {self.pos}")
            self.moves += 1
        return True

    def turn_direction_right(self):
        if self.direction is None:
            raise ValueError("Direction not set")
        # apply rotation matrix to turn right
        self.direction = (self.direction[1], -self.direction[0])

    def __str__(self):
        return f"Maze(pos={self.pos}, direction={self.direction}, moves={self.moves})"


def count_path(data:str) -> int:
    maze = parse_input(data)
    maze.find_position()
    moving = True 
    while moving:
        moving = maze.move()
    print(maze.visited_positions)
    return len(maze.visited_positions)

def create_paradox(data:str) -> int:
    maze = parse_input(data)
    maze.find_position()


def parse_input(data:str) -> Maze:
    maze = Maze(maze=[list(line) for line in data.split("\n")], pos=None)
    return maze

def main():
    with open("input.txt") as f:
        data = f.read()
    print(count_path(data))
    print(create_paradox(data))

if __name__ == "__main__":
    main()
