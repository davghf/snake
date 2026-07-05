
import pygame
from enum import Enum

screen_width: float = 640
screen_height: float = 480

music_level: int = 5
sfx_level: int = 5


# Resolutions: 640 x 480, 960 x 720, 1280 x 960
class Resolution(Enum):
    R_640_X_480 = 0
    R_960_X_720 = 1
    R_1280_X_960 = 2

screen_resolution: Resolution = Resolution.R_640_X_480



ui_font: pygame.Font | None = None

def get_ui_font() -> pygame.Font:
    global ui_font
    if ui_font is None:
        ui_font = pygame.font.Font("res/fonts/determination.ttf", size=12)
    return ui_font


class GameState(Enum):
    MAIN_MENU = 1
    OPTIONS_MENU = 3
    GAME = 2
    LEVEL_SELECTION = 4


class Action(Enum):
    NOTHING = 0
    QUIT = 1
    GO_TO_MAIN_MENU = 2
    GO_TO_OPTIONS_MENU = 3
    GO_TO_LEVEL_SELECTOR = 8
    GO_TO_GAME = 4
    UPDATE_RESOLUTION = 5
    UPDATE_MUSIC_LEVEL = 6
    UPDATE_SFX_LEVEL = 7