from random import randrange
import pygame


class Apple:
    def __init__(self, sg):
        self.screen = sg.screen
        self.settings = sg.settings

        self.pos_x = randrange(self.settings.size_block, self.settings.width -
                               self.settings.size_block, self.settings.size_block)
        self.pos_y = randrange(self.settings.size_block, self.settings.height -
                               self.settings.size_block, self.settings.size_block)

    def draw_apple(self):
        pygame.draw.rect(self.screen, self.settings.RED, (self.pos_x,
                         self.pos_y, self.settings.size_block, self.settings.size_block))

    def get_apple_coord(self):
        self.pos_x = randrange(self.settings.size_block, self.settings.width -
                               self.settings.size_block, self.settings.size_block)
        self.pos_y = randrange(self.settings.size_block, self.settings.height -
                               self.settings.size_block, self.settings.size_block)
