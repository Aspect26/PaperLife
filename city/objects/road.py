import pygame
from pygame.rect import Rect

from city.growth import GrowthFactor
from city.objects.city_object import CityObject
from game.constants import GameSettings

IMAGE_ALL = 'road_4.png'
IMAGE_THREE = 'road_3.png'
IMAGE_TWO_STRAIGHT = 'road_2s.png'
IMAGE_TWO_RIGHT_ANGLE = 'road_2ra.png'

_ROAD_IMAGE_MAP = {
    '0000': (IMAGE_TWO_STRAIGHT, 0),
    '0001': (IMAGE_TWO_STRAIGHT, 0),
    '0010': (IMAGE_TWO_STRAIGHT, 90),
    '0011': (IMAGE_TWO_RIGHT_ANGLE, 180),
    '0100': (IMAGE_TWO_STRAIGHT, 0),
    '0101': (IMAGE_TWO_STRAIGHT, 0),
    '0110': (IMAGE_TWO_RIGHT_ANGLE, 90),
    '0111': (IMAGE_THREE, 180),
    '1000': (IMAGE_TWO_STRAIGHT, 90),
    '1001': (IMAGE_TWO_RIGHT_ANGLE, 270),
    '1010': (IMAGE_TWO_STRAIGHT, 90),
    '1011': (IMAGE_THREE, 270),
    '1100': (IMAGE_TWO_RIGHT_ANGLE, 0),
    '1101': (IMAGE_THREE, 0),
    '1110': (IMAGE_THREE, 90),
    '1111': (IMAGE_ALL, 0),
}


class Road(CityObject):
    def __init__(self, city):
        position = Rect(0, 0, 1, 1)
        super().__init__(city, 100, position, 0, GrowthFactor(0, 0), 'road_2s.png', '')

    def render(self, screen: pygame.Surface) -> None:
        self.update_my_image(
            screen)  # TODO: this should be really called only when a building around myself is built and game load

    def update_my_image(self, screen: pygame.Surface):
        surrounding = list('0000')
        if isinstance(self.city.get_object_at((self.position.x - 1, self.position.y)), Road):
            surrounding[1] = '1'
        if isinstance(self.city.get_object_at((self.position.x + 1, self.position.y)), Road):
            surrounding[3] = '1'
        if isinstance(self.city.get_object_at((self.position.x, self.position.y - 1)), Road):
            surrounding[0] = '1'
        if isinstance(self.city.get_object_at((self.position.x, self.position.y + 1)), Road):
            surrounding[2] = '1'

        image, angle = _ROAD_IMAGE_MAP[''.join(surrounding)]
        building_picture = pygame.image.load(GameSettings.Paths.Images.CityObjects + image)
        building_picture = pygame.transform.scale(building_picture, (
            self.width * GameSettings.Game.FIELD_SIZE, self.height * GameSettings.Game.FIELD_SIZE))
        building_picture = pygame.transform.rotate(building_picture, angle)
        screen.blit(building_picture, (self.x * GameSettings.Game.FIELD_SIZE, self.y * GameSettings.Game.FIELD_SIZE))
