from random import randrange
import pygame


class Snake:
    def __init__(self, sg):
        self.screen = sg.screen
        self.settings = sg.settings

        self.pos_x = randrange(self.settings.size_block,
                               self.settings.width - self.settings.size_block, self.settings.size_block)
        self.pos_y = randrange(self.settings.size_block, self.settings.height -
                               self.settings.size_block, self.settings.size_block)

        self.snake_coord = [(self.pos_x, self.pos_y)]

        self.snake_len = 1

        self.dx, self.dy = 0, 0

        self.dic_direction = {'UP': (0, -1), 'DOWN': (0, 1),
                              'LEFT': (-1, 0), 'RIGHT': (1, 0)}

    def draw_snake(self):
        for x, y in self.snake_coord:
            pygame.draw.rect(self.screen, self.settings.GREEN, (x,
                             y, self.settings.size_block, self.settings.size_block))
            pygame.draw.rect(self.screen, self.settings.BLACK, (x,
                             y, self.settings.size_block, self.settings.size_block), 1)
        pygame.draw.rect(self.screen, self.settings.WHITE, (self.snake_coord[0][0],
                                                            self.snake_coord[0][1], self.settings.size_block, self.settings.size_block))

    def move(self):
        self.pos_x = (self.pos_x + self.dx *
                      self.settings.size_block) % self.settings.width
        self.pos_y = (self.pos_y + self.dy *
                      self.settings.size_block) % self.settings.height
        self.snake_coord.insert(0, (self.pos_x, self.pos_y))
        if len(self.snake_coord) > self.snake_len:
            self.snake_coord.pop()

    def turn(self, direction):
        x, y = self.dic_direction[direction]
        if self.snake_len > 1 and (x * -1, y * -1) == (self.dx, self.dy):
            return
        else:
            self.dx, self.dy = self.dic_direction[direction]
