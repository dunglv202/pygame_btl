import pygame
from os import path
from direction import Direction
from threading import Timer


class Item(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direction = Direction.TO_RIGHT
        self.speed = 5

    def apply(self, craft):
        self.kill()

    def unapply(self, craft):
        pass

    def update(self):
        # update position
        if self.direction == Direction.TO_RIGHT:
            self.rect.left += self.speed
        elif self.direction == Direction.TO_LEFT:
            self.rect.left -= self.speed
        elif self.direction == Direction.TO_TOP:
            self.rect.top -= self.speed
        elif self.direction == Direction.TO_BOTTOM:
            self.rect.top -= self.speed

        # check if out of range
        if not pygame.display.get_surface().get_rect().contains(self.rect):
            self.kill()


class ExpirableItem(Item):
    def __init__(self, expire_in_seconds: int):
        super().__init__()
        self.expire_in = expire_in_seconds

    def apply(self, craft):
        super().apply(craft)
        Timer(self.expire_in, self.unapply, [craft]).start()
