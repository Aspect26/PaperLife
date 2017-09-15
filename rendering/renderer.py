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
        for city_object in city.get_city_objects():
            # TODO: introduce image caching
            building_picture = pygame.image.load(city_object.image_path)
            building_picture = pygame.transform.scale(building_picture, (
                city_object.width * GameSettings.Game.FIELD_SIZE, city_object.height * GameSettings.Game.FIELD_SIZE))
            self._screen.blit(building_picture,
                              (city_object.x * GameSettings.Game.FIELD_SIZE, city_object.y * GameSettings.Game.FIELD_SIZE))

    def _render_ui(self, ui: UI):
        ui.render(self._screen)

    def _apply_render(self) -> None:
        pygame.display.flip()
