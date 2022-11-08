import pygame
from constant import *
from direction import Direction
from item import Item


class Bullet(Item):
    def __init__(self, direction: Direction, coord: list):
        super().__init__()

        self.direction = direction
        self.speed = 7
        self.damage = 1

        self.image = pygame.Surface((20, 5)).convert_alpha()
        self.image.fill("Red")
        self.rect = self.image.get_rect(center=coord)

    def apply(self, craft):
        if not self in craft.bullets:
            super().apply(craft)
            craft.hit(self)
