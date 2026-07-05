import pygame

from src.pygame.config import get_ui_font

class Selector:
    __hovered: bool
    __texts: list[str]

    __integer_interval: bool
    __min_value: int
    __max_value: int

    __cur_value: int

    __base_width: float = 120
    __base_height: float = 40

    surface: pygame.Surface

    def __init__(self, texts: list[str] = [], integer_interval: bool = False, min_value: int = 0, max_value: int = 0, init_value: int = 0, hovered: bool = False) -> None:
        self.__hovered = hovered
        self.__texts = texts
        self.__min_value = min_value
        self.__max_value = max_value
        self.__cur_value = init_value
        self.__integer_interval = integer_interval
        self.update()


    def increase_value(self):
        if self.__integer_interval:
            self.__cur_value = min(self.__max_value, self.__cur_value + 1)
        else:
            self.__cur_value = (self.__cur_value + 1) % len(self.__texts)

        self.update()


    def decrease_value(self):
        if self.__integer_interval:
            self.__cur_value = max(self.__min_value, self.__cur_value - 1)
        else:
            self.__cur_value = (self.__cur_value - 1)
            if self.__cur_value < 0:
                self.__cur_value = len(self.__texts) - 1
                
        self.update()


    def update(self, hovered: bool | None = None):
        if hovered is not None:
            self.__hovered = hovered

        width = self.__base_width
        height = self.__base_height
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surface.fill(pygame.Color(255, 255, 255))
        border_width = 2
        
        if self.__hovered:
            bg_color = pygame.Color(70, 70, 70)
        else:
            bg_color = pygame.Color(0, 0, 0)

        self.surface.fill(bg_color, pygame.Rect(border_width, border_width, width - 2 * border_width, height - 2 * border_width))
        font = get_ui_font()

        printed_text = None
        if self.__integer_interval:
            printed_text = font.render(str(self.__cur_value), False, (255, 255, 255))
        else:
            printed_text = font.render(self.__texts[self.__cur_value], False, (255, 255, 255))

        self.surface.blit(printed_text, ((width - printed_text.width) / 2, (height - printed_text.height) / 2 + 2))
