import pygame
from craft import Craft
from item import ExpirableItem
from os import path
from threading import Timer


class Shield(ExpirableItem):
    def __init__(self):
        super().__init__(3)
        self.image = pygame.transform.scale(pygame.image.load(
            path.join('graphics', 'shield.png')), (30, 30))
        self.rect = self.image.get_rect()

    def apply(self, craft: Craft):
        super().apply(craft)
        craft.has_shield = True
        print('Get shield -> health: ', craft.heath)

    def unapply(self, craft):
        craft.has_shield = False

    def kill(self) -> None:
        super().kill()
