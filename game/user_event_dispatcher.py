import pygame
from pygame.event import Event


class UserEventDispatcher(object):

    def __init__(self, game_object):
        self._game_object = game_object

    def dispatch(self, event: Event) -> None:
        if event.type == pygame.QUIT:
            self._game_object.exit_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self._game_object.handle_mouse_down(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            self._game_object.handle_mouse_up(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g:
                self._game_object.toggle_grid()
            elif event.key == pygame.K_b:
                self._game_object.toggle_buildings_window()
