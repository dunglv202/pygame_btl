from os import path
import pygame
from constant import WINDOW_HEIGHT, WINDOW_WIDTH
from direction import Direction
from pygame import Rect
from bullet import Bullet

class Craft(pygame.sprite.Sprite):
    def __init__(self, image: str, direction: Direction, bound: Rect, controls: dict):
        super().__init__()

        # define statistic for craft
        self.moving_speed = 7
        self.heath = 10
        self.has_shield = False
        self.controls = controls
        self.bullets = list()
        self.direction = direction
        self.bound = bound

        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(path.join('graphics', image)), (120, 120)), (90 if direction == Direction.TO_LEFT else -90)).convert_alpha()
        self.rect = self.image.get_rect()
        if direction == Direction.TO_LEFT:
            self.rect.midright = bound.midright
        else:
            self.rect.midleft = bound.midleft

    def handle_user_input(self, key_pressed):
        if key_pressed[self.controls['up']] and self.rect.top - self.moving_speed > self.bound.top:
            self.rect.top -= self.moving_speed
        if key_pressed[self.controls['down']] and self.rect.bottom + self.moving_speed < self.bound.bottom:
            self.rect.top += self.moving_speed
        if key_pressed[self.controls['left']] and self.rect.left - self.moving_speed > self.bound.left:
            self.rect.left -= self.moving_speed
        if key_pressed[self.controls['right']] and self.rect.right + self.moving_speed < self.bound.right:
            self.rect.left += self.moving_speed

    def fire(self, bullet_group: pygame.sprite.Group):
        print("Fired!")
        if self.alive() and len(self.bullets) < 5:
            new_bullet = Bullet(self.direction, self.rect.center)
            self.bullets.append(new_bullet)
            bullet_group.add(new_bullet)

    def hit(self, bullet: Bullet):
        if self.has_shield:
            self.has_shield = False
        else:
            self.heath -= bullet.damage
        print('get hit! health: ', self.heath)

    def update(self):
        if self.heath <= 0:
            self.kill()
        for bullet in self.bullets:
            if not bullet.alive():
                self.bullets.remove(bullet)