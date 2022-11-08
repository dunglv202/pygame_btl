import sys
import pygame
from pygame import *
from confuser import Confuser
from craft import Craft
from direction import Direction
from booster import Booster
from shield import Shield
import random


class SpaceShooting:
    def __init__(self, width, height, fps, options):
        pygame.init()
        # init game screen
        self.screen = pygame.display.set_mode(
            (width, height), options)
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.paused = False
        # init background
        self.background = pygame.transform.scale(pygame.image.load(
            'graphics/space.png'), (self.screen.get_width(), self.screen.get_height())).convert_alpha()
        # add crafts
        self.blue_craft = Craft(
            image='craft_blue.png',
            direction=Direction.TO_BOTTOM,
            bound=pygame.Rect(0, 0, self.screen.get_width(),
                              self.screen.get_height()/2),
            controls={'up': K_w, 'down': K_s, 'left': K_a,
                      'right': K_d, 'fire': K_BACKQUOTE}
        )
        self.red_craft = Craft(
            image='craft_red.png',
            direction=Direction.TO_TOP,
            bound=pygame.Rect(0, self.screen.get_height()/2,
                              self.screen.get_width(), self.screen.get_height()/2),
            controls={'up': K_UP, 'down': K_DOWN, 'left': K_LEFT,
                      'right': K_RIGHT, 'fire': K_RETURN}
        )
        self.craft_group = pygame.sprite.Group()
        self.craft_group.add(self.blue_craft)
        self.craft_group.add(self.red_craft)
        # declare bullet group
        self.bullet_group = pygame.sprite.Group()
        # item group
        self.item_group = pygame.sprite.Group()
        # available item list
        self.available_items = [Shield, Booster, Confuser]

    def show_main_menu(self):
        pass

    def loop_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    key_pressed = pygame.key.get_pressed()

                    # check for pausing
                    if key_pressed[K_p] or key_pressed[K_ESCAPE]:
                        self.pause_game()

                    if self.paused:
                        continue

                    # check for firing
                    if key_pressed[self.blue_craft.controls['fire']]:
                        self.blue_craft.fire(self.item_group)
                    if key_pressed[self.red_craft.controls['fire']]:
                        self.red_craft.fire(self.item_group)

            if self.paused:
                continue

            # draw background
            self.screen.blit(self.background, (0, 0))

            # add item
            if random.randint(0, 1000) > 990:
                item = random.choice(self.available_items)()
                item.rect.top = random.randint(0, self.screen.get_height())
                self.item_group.add(item)

            # handle user input
            key_pressed = pygame.key.get_pressed()
            self.blue_craft.handle_user_input(key_pressed)
            self.red_craft.handle_user_input(key_pressed)

            # detect collisions
            # self.bullet_group.update()
            self.craft_group.update()
            self.item_group.update()
            for craft in self.craft_group:
                items_colliding = pygame.sprite.spritecollide(
                    craft, self.item_group, False)
                for item in items_colliding:
                    item.apply(craft)

            # update frames
            self.__update__()
            self.clock.tick(self.fps)

    def pause_game(self):
        self.paused = not self.paused

    def __update__(self):
        # self.bullet_group.draw(self.screen)
        self.item_group.draw(self.screen)
        self.craft_group.draw(self.screen)
        pygame.display.update()
