from os import path
import pygame

WINDOW_WIDTH = 920
WINDOW_HEIGHT = 640

class Background(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()

    self.image = pygame.transform.scale(pygame.image.load(path.join('graphics', 'space.png')), (WINDOW_WIDTH, WINDOW_HEIGHT)).convert_alpha()
    self.rect = self.image.get_rect()