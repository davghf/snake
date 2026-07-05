from dataclasses import dataclass
from enum import Enum

class Tile(Enum):
    EMPTY = 0
    SNAKE = 1
    BLOCK = 2
    PRIZE = 3


class SnakeSegment:
    is_head: bool
    is_tail: bool
    next_segment: "SnakeSegment | None"
    previous_segment: "SnakeSegment | None"

    def __init__(self, is_head: bool = False, is_tail: bool = False, 
                 next_segment: "SnakeSegment | None" = None,
                 previous_segment: "SnakeSegment | None" = None) -> None:
        self.is_head = is_head
        self.is_tail = is_tail
        self.next_segment = next_segment
        self.previous_segment = previous_segment

    def update(self, next_segment: "SnakeSegment | None" = None,
               previous_segment: "SnakeSegment | None" = None):
        pass


@dataclass
class Level:
    objective_level: int
    duration: int
    name: str
    max_score: int
    field: list[list[int]]


class Core:
    levels: list[Level] = []
    field: list[list[Tile]]

    __advance_dir: tuple[int, int]
    __turns_per_movement: int = 2


    def set_advance_dir(self):
        pass

    def load_level(self):
        pass

    def pass_turn(self):
        pass