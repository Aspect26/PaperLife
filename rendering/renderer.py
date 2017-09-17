import pygame

from city.city import City
from game.constants import GameSettings
from rendering.image_cache import get_image
from ui.ui import UI


# TODO: remove this class -> the rendering will be directly in the City class
class Renderer:
    def __init__(self, width, height):
        self._screen = pygame.display.set_mode((width, height))

    def render(self, city: City, ui: UI) -> None:
        self._render_background()
        self._render_city(city)
        self._render_ui(ui)
        self._apply_render()

    def _render_background(self) -> None:
        background_image = get_image(GameSettings.Paths.Images.Background)
        background_image = pygame.transform.scale(background_image,
                                                  (GameSettings.Screen.WIDTH, GameSettings.Screen.HEIGHT))
        self._screen.blit(background_image, (0, 0))

    def _render_city(self, city: City) -> None:
        for city_object in city.get_city_objects():
            # TODO: introduce image caching
            city_object.render(self._screen)

    def _render_ui(self, ui: UI):
        ui.render(self._screen)

    def _apply_render(self) -> None:
        pygame.display.flip()
