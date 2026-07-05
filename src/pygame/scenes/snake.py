import pygame
from logic.core import Core
from src.pygame.config import Action, screen_width, screen_height

class Snake:
    
    surface: pygame.Surface
    width: float = screen_width
    height: float = screen_height

    __acc_time: float = 0
    __trigger_time: float = 0.5

    __core: Core


    def __init__(self) -> None:
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)


    def check_events(self, events: list[pygame.Event]) -> Action:
        return Action.NOTHING


    def update(self):
        self.surface.fill(pygame.Color(0, 0, 0))
