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
    next_segment: "SnakeSegment"
    previous_segmente: "SnakeSegment"

    def __init__(self, is_head: bool = False, is_tail: bool = False) -> None:
        self.is_head = is_head
        self.is_tail = is_tail


@dataclass
class Level:
    objective_level: int
    duration: int
    name: str
    max_score: int


class Core:
    levels: list[Level] = []
    
    pass

    def set_level(self):
        pass

    def move_snake(self):
        pass