import pygame

from city.city import City
from constants import GameSettings


class Renderer:
    def __init__(self, width, height):
        self._screen = pygame.display.set_mode((width, height))

    def render(self, city: City) -> None:
        self._render_background()
        self._render_money(city)
        self._render_city(city)
        self._apply_render()

    def _render_background(self) -> None:
        self._screen.fill((255, 255, 255))

    def _render_money(self, city: City) -> None:
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render('Money: ' + str(city.get_money()), 1, (255, 0, 0))
        self._screen.blit(label, (10, 10))

    def _render_city(self, city: City) -> None:
        for building in city.get_buildings():
            self._screen.blit(pygame.image.load(building.image_path),
                              (building.x * GameSettings.Game.FIELD_SIZE, building.y * GameSettings.Game.FIELD_SIZE))

    def _apply_render(self) -> None:
        pygame.display.flip()
