
from enum import Enum

screen_width: float = 640
screen_height: float = 480


# Resolutions: 640 x 480, 960 x 720, 1280 x 960
class Resolution(Enum):
    R_640_X_480 = 0
    R_960_X_720 = 1
    R_1280_X_960 = 2

screen_resolution: Resolution = Resolution.R_640_X_480


class GameState(Enum):
    MAIN_MENU = 1
    OPTIONS_MENU = 3
    GAME = 2


class Action(Enum):
    NOTHING = 0
    QUIT = 1
    GO_TO_MAIN_MENU = 2
    GO_TO_OPTIONS_MENU = 3
    GO_TO_GAME = 4
    UPDATE_RESOLUTION = 5