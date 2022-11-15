import pygame
from constant import *
from direction import Direction
from item import Item
from os import path


class Obstacle(Item):
    def __init__(self):
        super().__init__()

        self.direction = Direction.TO_RIGHT
        self.speed = 7
        self.damage = 1

        self.image = pygame.transform.scale(pygame.image.load(
            path.join('graphics', 'obstacle.png')), (30, 30)).convert_alpha()
        self.rect = self.image.get_rect()

    def apply(self, craft):
        if not self in craft.bullets:
            super().apply(craft)
            craft.hit(self)
