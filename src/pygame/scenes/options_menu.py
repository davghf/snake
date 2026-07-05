import pygame
from enum import Enum

from src.pygame.components.selector import Selector
from src.pygame import config
from src.pygame.config import Action, screen_width, screen_height, Resolution

from src.pygame.components.button import Button


class SelectedButton(Enum):
    RESOLUTION = 1
    EXIT = 2
    SFX = 3
    MUSIC = 4


class OptionsMenu:
    surface: pygame.Surface
    width: float = screen_width
    height: float = screen_height

    def __init__(self) -> None:
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.resolution_button = Button("Resolution")
        self.resolution_selector = Selector(texts=["640 x 480", "960 x 720", "1280 x 960"])

        self.sfx_button = Button("SFX")
        self.sfx_selector = Selector(integer_interval=True, min_value=0, max_value=10, init_value=5)

        self.music_button = Button("MUSIC")
        self.music_selector = Selector(integer_interval=True, min_value=0, max_value=10, init_value=5)
        
        self.exit_button = Button("Go Back")

        self.selected_button = SelectedButton.RESOLUTION


    def check_events(self, events: list[pygame.Event]) -> Action:
        for event in events:
            if event.type == pygame.QUIT:
                return Action.QUIT
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    match self.selected_button:
                        case SelectedButton.RESOLUTION:
                            pass
                        case SelectedButton.EXIT:
                            return Action.GO_TO_MAIN_MENU
                else:
                    up_released = event.key == pygame.K_UP 
                    down_released = event.key == pygame.K_DOWN
                    left_released = event.key == pygame.K_LEFT
                    right_released = event.key == pygame.K_RIGHT

                    if up_released and not down_released:
                        match self.selected_button:
                            case SelectedButton.RESOLUTION:
                                self.selected_button = SelectedButton.EXIT
                            case SelectedButton.EXIT:
                                self.selected_button = SelectedButton.MUSIC
                            case SelectedButton.MUSIC:
                                self.selected_button = SelectedButton.SFX
                            case SelectedButton.SFX:
                                self.selected_button = SelectedButton.RESOLUTION
                    elif not up_released and down_released:
                        match self.selected_button:
                            case SelectedButton.RESOLUTION:
                                self.selected_button = SelectedButton.SFX
                            case SelectedButton.EXIT:
                                self.selected_button = SelectedButton.RESOLUTION
                            case SelectedButton.MUSIC:
                                self.selected_button = SelectedButton.EXIT
                            case SelectedButton.SFX:
                                self.selected_button = SelectedButton.MUSIC

                    elif left_released and not right_released:
                        match self.selected_button:
                            case SelectedButton.RESOLUTION:
                                self.__prev_resolution()
                                return Action.UPDATE_RESOLUTION
                            case SelectedButton.MUSIC:
                                self.music_selector.decrease_value()
                                return Action.UPDATE_MUSIC_LEVEL
                            case SelectedButton.SFX:
                                self.sfx_selector.decrease_value()
                                return Action.UPDATE_SFX_LEVEL
                            case _:
                                pass
                    elif not left_released and right_released:
                        match self.selected_button:
                            case SelectedButton.RESOLUTION:
                                self.__next_resolution()
                                return Action.UPDATE_RESOLUTION
                            case SelectedButton.MUSIC:
                                self.music_selector.increase_value()
                                return Action.UPDATE_MUSIC_LEVEL
                            case SelectedButton.SFX:
                                self.sfx_selector.increase_value()
                                return Action.UPDATE_SFX_LEVEL
                            case _:
                                pass

        return Action.NOTHING
        

    def __next_resolution(self):
        match config.screen_resolution:
            case Resolution.R_640_X_480:
                config.screen_resolution = Resolution.R_960_X_720
            case Resolution.R_960_X_720:
                config.screen_resolution = Resolution.R_1280_X_960
            case Resolution.R_1280_X_960:
                config.screen_resolution = Resolution.R_640_X_480

        self.resolution_selector.increase_value()

    
    def __prev_resolution(self):
        match config.screen_resolution:
            case Resolution.R_640_X_480:
                config.screen_resolution = Resolution.R_1280_X_960
            case Resolution.R_960_X_720:
                config.screen_resolution = Resolution.R_640_X_480
            case Resolution.R_1280_X_960:
                config.screen_resolution = Resolution.R_960_X_720

        self.resolution_selector.decrease_value()


    def update(self):
        self.surface.fill(pygame.Color(0, 0, 0))

        self.resolution_button.update(hovered=False)
        self.exit_button.update(hovered=False)
        self.sfx_button.update(hovered=False)
        self.music_button.update(hovered=False)

        match self.selected_button:
            case SelectedButton.EXIT:
                self.exit_button.update(hovered=True)
            case SelectedButton.RESOLUTION:
                self.resolution_button.update(hovered=True)
            case SelectedButton.MUSIC:
                self.music_button.update(hovered=True)
            case SelectedButton.SFX:
                self.sfx_button.update(hovered=True)
            

        left_margin = 150

        self.surface.blit(self.resolution_button.surface, (left_margin, 100))
        self.surface.blit(self.resolution_selector.surface, (left_margin + 200, 100))

        self.surface.blit(self.sfx_button.surface, (left_margin, 200))
        self.surface.blit(self.sfx_selector.surface, (left_margin + 200, 200))

        self.surface.blit(self.music_button.surface, (left_margin, 300))
        self.surface.blit(self.music_selector.surface, (left_margin + 200, 300))

        self.surface.blit(self.exit_button.surface, (left_margin, 400))