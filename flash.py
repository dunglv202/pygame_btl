from os import path
import pygame
from item import Item

class Flash(Item):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(path.join('graphics', 'craft_red.png')), (30, 30))
        self.rect = self.image.get_rect()

    def apply(self, craft):
        super().apply(craft)
        craft.moving_speed = 15

    def update(self):
        super().update()
        self.rect.top += self.speed