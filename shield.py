import pygame
from craft import Craft
from item import Item
from os import path

class Shield(Item):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path.join('graphics', 'craft_red.png')), (30, 30))
        self.rect = self.image.get_rect()

    def apply(self, craft: Craft):
        super().apply(craft)
        craft.has_shield = True
        print('Get shield -> health: ', craft.heath)

    def update(self):
        super().update()
        self.rect.top += self.speed

    def kill(self) -> None:
        super().kill()
