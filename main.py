import pygame
from constant import *
from space_shooting import SpaceShooting

if __name__ == '__main__':
    space_shooting = SpaceShooting(
        WINDOW_WIDTH, WINDOW_HEIGHT, FPS, pygame.SHOWN)
    space_shooting.run()
