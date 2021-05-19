import pygame.font


class ScoreBoard:

    def __init__(self, sg):
        self.screen = sg.screen
        self.settings = sg.settings
        self.screen_rect = self.screen.get_rect()

        self.score = 0
        self.high_score = 0
        self.font = pygame.font.SysFont('comicsans', 30)

    def draw_score_and_control(self):
        self.get_score()
        self.get_high_score()
        self.get_control()

    def get_score(self):
        score = self.score
        render_score = self.font.render(
            f'Score: {score}', True, self.settings.WHITE)
        self.screen.blit(render_score, (5, 0))

    def get_control(self):
        control_str = 'Up, Left, Down, Right'
        self.control_image = self.font.render(
            control_str, True, self.settings.WHITE)

        self.control_rect = self.control_image.get_rect()
        self.control_rect.midbottom = self.screen_rect.midbottom

        self.screen.blit(self.control_image, self.control_rect)

    def get_high_score(self):
        self.check_high_score()
        high_score = self.high_score
        render_hscore = self.font.render(
            f'High score: {high_score}', True, self.settings.WHITE)
        self.screen.blit(render_hscore, (self.settings.width - 155, 0))

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
