import pygame
from enum import Enum

from src.pygame import config
from src.pygame.config import Action, screen_width, screen_height, Resolution

from src.pygame.components.button import Button


class SelectedButton(Enum):
    RESOLUTION = 1
    EXIT = 2


class OptionsMenu:
    surface: pygame.Surface
    width: float = screen_width
    height: float = screen_height

    def __init__(self) -> None:
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.resolution_button = Button("Resolution")
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

                    if up_released != down_released:
                        match self.selected_button:
                            case SelectedButton.RESOLUTION:
                                self.selected_button = SelectedButton.EXIT
                            case SelectedButton.EXIT:
                                self.selected_button = SelectedButton.RESOLUTION
                    elif left_released and not right_released:
                        match config.screen_resolution:
                            case Resolution.R_640_X_480:
                                config.screen_resolution = Resolution.R_1280_X_960
                            case Resolution.R_960_X_720:
                                config.screen_resolution = Resolution.R_640_X_480
                            case Resolution.R_1280_X_960:
                                config.screen_resolution = Resolution.R_960_X_720

                        return Action.UPDATE_RESOLUTION
                    elif not left_released and right_released:
                        match config.screen_resolution:
                            case Resolution.R_640_X_480:
                                config.screen_resolution = Resolution.R_960_X_720
                            case Resolution.R_960_X_720:
                                config.screen_resolution = Resolution.R_1280_X_960
                            case Resolution.R_1280_X_960:
                                config.screen_resolution = Resolution.R_640_X_480

                        return Action.UPDATE_RESOLUTION

        return Action.NOTHING
        
    
    def update(self):
        self.surface.fill(pygame.Color(0, 0, 0))

        self.resolution_button.update(hovered=False)
        self.exit_button.update(hovered=False)

        match self.selected_button:
            case SelectedButton.EXIT:
                self.exit_button.update(hovered=True)
            case SelectedButton.RESOLUTION:
                self.resolution_button.update(hovered=True)

        self.surface.blit(self.resolution_button.surface, (100, 100))
        self.surface.blit(self.exit_button.surface, (100, 200))