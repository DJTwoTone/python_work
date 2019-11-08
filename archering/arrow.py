import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):

    def __init__(self, ai_settings, screen, archer):

        super(Arrow, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, ai_settings.arrow_width, ai_settings.arrow_height)
        self.rect.centery = archer.rect.centery
        self.rect.right = archer.rect.right

        self.x = float(self.rect.x)

        self.color = ai_settings.arrow_color
        self.speed_factor = ai_settings.arrow_speed_factor

    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_arrow(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

