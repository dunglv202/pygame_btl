import pygame
from os import path

class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 7

    def apply(self, craft):
        self.kill()

    def update(self):
        # check if out of range
        if not pygame.display.get_surface().get_rect().contains(self.rect):
            self.kill()