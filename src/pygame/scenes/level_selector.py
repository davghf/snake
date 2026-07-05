import pygame
from enum import Enum

from src.pygame.components.button import Button
from src.pygame.components.level_block import LevelBlock
from src.pygame.config import screen_width, screen_height, Action


class LevelSelector:
    surface: pygame.Surface
    width: float = screen_width
    height: float = screen_height

    page: int = 0
    position: int = 0


    def __init__(self) -> None:
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.level_1_block = LevelBlock("Mission 1: First Steps", "Objective: Reach Level 20", 90, "EASY")
        self.back_button = Button("Go Back")
        
        self.update()


    def check_events(self, events: list[pygame.Event]) -> Action:
        for event in events:
            if event.type == pygame.QUIT:
                return Action.QUIT
            
        return Action.NOTHING


    def update(self):
        self.surface.fill(pygame.Color(0, 0, 0))

        self.level_1_block.update(hovered=False)

        left_margin = (640 - 420) / 2

        self.surface.blit(self.level_1_block.surface, (left_margin, 100))