from pygame import Surface
import pygame
from os import path

class Button(Surface):
    def __init__(self, image, width, height):
        super().__init__((width, height))
        image = pygame.transform.scale(pygame.image.load(path.join('graphics', image)), (width, height)).convert_alpha()
        self.blit(image, (0, 0))
        self.rect = (0, 0)

    def set_onclick(self, callback):
        self.onclick = callback

    def click(self):
        self.onclick()