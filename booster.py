from os import path
import pygame
from item import ExpirableItem


class Booster(ExpirableItem):
    def __init__(self):
        super().__init__(5)
        self.image = pygame.transform.scale(pygame.image.load(
            path.join('graphics', 'craft_red.png')), (30, 30))
        self.rect = self.image.get_rect()

    def apply(self, craft):
        super().apply(craft)
        self.original_speed = craft.moving_speed
        craft.moving_speed = 15

    def unapply(self, craft):
        craft.moving_speed = self.original_speed
