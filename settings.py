import pygame


class Settings:
    def __init__(self):
        self.width = 420
        self.height = 600
        self.size_block = 20

        self.FPS = 7
        self.fps_clock = pygame.time.Clock()

        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        self.snake_speed = 1
