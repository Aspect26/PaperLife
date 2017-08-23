import pygame

from city.city import City
from game.constants import GameSettings
from ui.ui import UI


class Renderer:
    def __init__(self, width, height):
        self._screen = pygame.display.set_mode((width, height))

    def render(self, city: City, ui: UI) -> None:
        self._render_background()
        self._render_city(city)
        self._render_ui(ui)
        self._apply_render()

    def _render_background(self) -> None:
        background_image = pygame.image.load(GameSettings.Paths.Images.Background)
        background_image = pygame.transform.scale(background_image,
                                                  (GameSettings.Screen.WIDTH, GameSettings.Screen.HEIGHT))
        self._screen.blit(background_image, (0, 0))

    def _render_city(self, city: City) -> None:
        for building in city.get_buildings():
            # TODO: introduce image caching
            building_picture = pygame.image.load(building.image_path)
            building_picture = pygame.transform.scale(building_picture, (
            building.width * GameSettings.Game.FIELD_SIZE, building.height * GameSettings.Game.FIELD_SIZE))
            self._screen.blit(building_picture,
                              (building.x * GameSettings.Game.FIELD_SIZE, building.y * GameSettings.Game.FIELD_SIZE))

    def _render_ui(self, ui: UI):
        ui.render(self._screen)

    def _apply_render(self) -> None:
        pygame.display.flip()
