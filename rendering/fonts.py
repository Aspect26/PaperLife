import pygame


class Fonts(object):

    _FONT_NAME = 'monospace'
    SMALL_FONT = pygame.font.SysFont(_FONT_NAME, 10)
    MEDIUM_FONT = pygame.font.SysFont(_FONT_NAME, 13)
    LARGE_FONT = pygame.font.SysFont(_FONT_NAME, 15)
