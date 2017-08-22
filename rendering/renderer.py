import pygame

from city.city import City


class Renderer:

    def __init__(self, width, height):
        self._screen = pygame.display.set_mode((width, height))

    def render(self, city: City) -> None:
        self._render_background()
        self._render_money(city)
        self._apply_render()

    def _render_background(self) -> None:
        self._screen.fill((255, 255, 255))

    def _render_money(self, city: City) -> None:
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render('Money: ' + str(city.get_money()), 1, (255, 0, 0))
        self._screen.blit(label, (10, 10))

    def _apply_render(self) -> None:
        pygame.display.flip()
