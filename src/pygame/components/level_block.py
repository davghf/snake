import pygame
import math

from src.pygame.config import get_ui_font


class LevelBlock:
    __hovered: bool
    __name: str
    __objective: str
    __time_limit: int
    __difficulty: str
    
    __base_width: float = 420
    __base_height: float = 80

    def __init__(self, name: str, objective: str, time_limit: int, difficulty: str) -> None:
        self.__hovered = False
        self.__name =  name
        self.__objective = objective
        self.__time_limit = time_limit
        self.__difficulty = difficulty
        self.update()

    
    def update(self, hovered: bool | None = None):
        if hovered is not None:
            self.__hovered = hovered

        width = self.__base_width
        height = self.__base_height
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)

        border_color = pygame.Color(255, 255, 255)
        self.surface.fill(border_color)
        border_width = 2
        
        if self.__hovered:
            bg_color = pygame.Color(70, 70, 70)
        else:
            bg_color = pygame.Color(0, 0, 0)

        self.surface.fill(bg_color, pygame.Rect(border_width, border_width, width - 2 * border_width, height - 2 * border_width))
        pygame.draw.line(self.surface, border_color, (340, 0), (340, 80), 2)
        pygame.draw.line(self.surface, border_color, (0, 40), (340, 40), 2)
        pygame.draw.line(self.surface, border_color, (190, 40), (190, 80), 2)

        font = get_ui_font()
        printed_text = font.render(self.__name, False, (255, 255, 255))
        self.surface.blit(printed_text, ((340 - printed_text.width) / 2, (40 - printed_text.height) / 2 + 2))
        printed_text = font.render(self.__objective, False, (255, 255, 255))
        self.surface.blit(printed_text, ((190 - printed_text.width) / 2, 40 + (40 - printed_text.height) / 2 + 2))

        minutes = math.floor(self.__time_limit / 60)
        seconds = self.__time_limit % 60
        msg: str = "Time Limit: " 
        if minutes > 0:
            msg += str(minutes) + "m"
            if seconds > 0:
                msg += " "
        if seconds > 0:
            msg = msg + str(seconds) + "s"

        printed_text = font.render(msg, False, (255, 255, 255))
        self.surface.blit(printed_text, (190 + (150 - printed_text.width) / 2, 40 + (40 - printed_text.height) / 2 + 2))

        printed_text = font.render(self.__difficulty, False, (255, 255, 255))
        self.surface.blit(printed_text, (340 + (80 - printed_text.width) / 2, (80 - printed_text.height) / 2 + 2))
