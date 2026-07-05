import pygame
from enum import Enum

from src.pygame.config import Action, screen_width, screen_height
from src.pygame.components.button import Button


class SelectedButton(Enum):
    START = 1
    OPTIONS = 2
    EXIT = 3


class MainMenu:
    surface: pygame.Surface
    width: float = screen_width
    height: float = screen_height

    def __init__(self) -> None:
        self.surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.start_button = Button("Start Game")
        self.options_button = Button("Options")
        self.exit_button = Button("Exit")

        self.selected_button = SelectedButton.START
        self.start_button.update(hovered=True)


    def check_events(self, events: list[pygame.Event]) -> Action:
        for event in events:
            if event.type == pygame.QUIT:
                return Action.QUIT
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == pygame.K_KP_ENTER:
                    match self.selected_button:
                        case SelectedButton.START:
                            return Action.GO_TO_LEVEL_SELECTOR
                        case SelectedButton.OPTIONS:
                            return Action.GO_TO_OPTIONS_MENU
                        case SelectedButton.EXIT:
                            return Action.QUIT
                elif event.key == pygame.K_UP and not event.key == pygame.K_DOWN:
                    match self.selected_button:
                        case SelectedButton.START:
                            self.selected_button = SelectedButton.EXIT
                        case SelectedButton.OPTIONS:
                            self.selected_button = SelectedButton.START
                        case SelectedButton.EXIT:
                            self.selected_button = SelectedButton.OPTIONS

                elif not event.key == pygame.K_UP and event.key == pygame.K_DOWN:
                    match self.selected_button:
                        case SelectedButton.START:
                            self.selected_button = SelectedButton.OPTIONS
                        case SelectedButton.OPTIONS:
                            self.selected_button = SelectedButton.EXIT
                        case SelectedButton.EXIT:
                            self.selected_button = SelectedButton.START

        return Action.NOTHING
        
    
    def update(self):
        self.surface.fill(pygame.Color(0, 0, 0))

        self.start_button.update(hovered=False)
        self.options_button.update(hovered=False)
        self.exit_button.update(hovered=False)

        match self.selected_button:
            case SelectedButton.START:
                self.start_button.update(hovered=True)
            case SelectedButton.OPTIONS:
                self.options_button.update(hovered=True)
            case SelectedButton.EXIT:
                self.exit_button.update(hovered=True)

        left_margin = 260

        self.surface.blit(self.start_button.surface, (left_margin, 100))
        self.surface.blit(self.options_button.surface, (left_margin, 200))
        self.surface.blit(self.exit_button.surface, (left_margin, 300))