import pygame

from src.pygame.scenes.level_selector import LevelSelector
from src.pygame import config
from src.pygame.config import Action, screen_width, screen_height, GameState, Resolution

from src.pygame.scenes.options_menu import OptionsMenu
from src.pygame.scenes.main_menu import MainMenu

# Resolutions: 640 x 480, 960 x 720, 1280 x 960

class Controller:

    scale: float = 1.0
    width: float = screen_width
    height: float = screen_height


    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.state = GameState.MAIN_MENU
        self.main_menu = MainMenu()
        self.options_menu = OptionsMenu()
        self.level_selector = LevelSelector()




        self.running = True
        self.clock = pygame.time.Clock()

        self.delta_time = 0.1

        # self.main_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)


    def run(self):

        while self.running:
            # self.screen.fill((0, 0, 0))
            # if self.state is GameState.MAIN_MENU:
            self.event_loop()

            scene = None
            match self.state:
                case GameState.MAIN_MENU:
                    self.main_menu.update()
                    scene = self.main_menu.surface
                case GameState.OPTIONS_MENU:
                    self.options_menu.update()
                    scene = self.options_menu.surface
                case GameState.LEVEL_SELECTION:
                    self.level_selector.update()
                    scene = self.level_selector.surface

            
            if scene is not None:
                scaled_scene = pygame.transform.scale(scene, (scene.width * self.scale, scene.height * self.scale))
                self.screen.blit(scaled_scene, (0, 0))

            pygame.display.update()

            self.delta_time = self.clock.tick(60) / 1000
            self.delta_time = max(0.001, min(0.1, self.delta_time))
            
        pygame.quit()


    def event_loop(self):
        events = pygame.event.get()

        action = Action.NOTHING
        match self.state:
            case GameState.MAIN_MENU:
                action = self.main_menu.check_events(events)
            case GameState.OPTIONS_MENU:
                action = self.options_menu.check_events(events)
            case GameState.LEVEL_SELECTION:
                action = self.level_selector.check_events(events)
            
        match action: 
            case Action.QUIT:
                self.running = False
            case Action.GO_TO_MAIN_MENU:
                self.state = GameState.MAIN_MENU
            case Action.GO_TO_LEVEL_SELECTOR:
                self.state = GameState.LEVEL_SELECTION
            case Action.GO_TO_OPTIONS_MENU:
                self.state = GameState.OPTIONS_MENU
            case Action.UPDATE_RESOLUTION:
                match config.screen_resolution:
                    case Resolution.R_640_X_480:
                        self.scale = 1.0
                    case Resolution.R_960_X_720:
                        self.scale = 1.5
                    case Resolution.R_1280_X_960:
                        self.scale = 2.0

                self.screen = pygame.display.set_mode((self.width * self.scale, self.height * self.scale))

