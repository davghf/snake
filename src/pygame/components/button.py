import pygame

button_font: pygame.Font | None = None

def get_button_font() -> pygame.Font:
    global button_font
    if button_font is None:
        button_font = pygame.font.Font("res/fonts/Minecraft.ttf", size=14)
    return button_font


class Button:
    __hovered: bool
    __text: str
    __base_width: float = 120
    __base_height: float = 40

    surface: pygame.Surface

    def __init__(self, text: str, hovered: bool = False) -> None:
        self.__hovered = hovered
        self.__text = text
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
        font = pygame.font.Font("res/fonts/Minecraft.ttf", size=round(14))
        printed_text = font.render(self.__text, False, (255, 255, 255))

        self.surface.blit(printed_text, ((width - printed_text.width) / 2, (height - printed_text.height) / 2 + 2))
