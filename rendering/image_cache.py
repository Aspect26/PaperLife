import pygame

_cached_images = {}


def get_image(path: str):
    if path in _cached_images:
        return _cached_images[path]
    _cached_images[path] = pygame.image.load(path)
    return _cached_images[path]
