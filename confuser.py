import pygame
from os import path
from item import ExpirableItem
from threading import Timer


class Confuser(ExpirableItem):
    def __init__(self):
        super().__init__(1)
        self.image = pygame.transform.scale(pygame.image.load(
            path.join('graphics', 'item.png')), (30, 30))
        self.rect = self.image.get_rect()

    def apply(self, craft):
        super().apply(craft)
        craft.reverse_controls()

    def unapply(self, craft):
        craft.reverse_controls()
