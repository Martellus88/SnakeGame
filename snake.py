from random import randrange
import sys
import pygame
from settings import Settings
from snake_cls import Snake
from apple import Apple
from scoreboard import ScoreBoard


class SnakeGame:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.width, self.settings.height))
        pygame.display.set_caption('Snake Game')

        self.snake = Snake(self)
        self.apple = Apple(self)
        self.sb = ScoreBoard(self)

    def run_game(self):

        while True:
            self.settings.fps_clock.tick(self.settings.FPS)

            self.screen.fill(self.settings.BLACK)

            self._check_events()
            self.snake.move()
            self.snake.draw_snake()
            self.apple.draw_apple()
            self.check_coll_apple()
            self.check_eat_yourself()
            self.sb.draw_score_and_control()
            pygame.display.update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.snake.turn('UP')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.snake.turn('DOWN')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.snake.turn('LEFT')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.snake.turn('RIGHT')

    def check_coll_apple(self):
        if self.snake.snake_coord[0] == (self.apple.pos_x, self.apple.pos_y):
            self.grow()
            self.apple.get_apple_coord()

    def grow(self):
        self.snake.snake_len += 1
        self.sb.score += 1
        self.settings.FPS += 0.5

    def check_eat_yourself(self):
        if self.snake.snake_coord[0] in self.snake.snake_coord[2:]:
            self.restart()

    def restart(self):
        self.snake.snake_len = 1
        self.snake.pos_x = randrange(self.settings.size_block,
                                     self.settings.width - self.settings.size_block, self.settings.size_block)
        self.snake.pos_y = randrange(self.settings.size_block, self.settings.height -
                                     self.settings.size_block, self.settings.size_block)

        self.snake.snake_coord = [(self.snake.pos_x, self.snake.pos_y)]
        self.sb.score = 0
        self.settings.FPS = 7


if __name__ == '__main__':
    sg = SnakeGame()
    sg.run_game()
