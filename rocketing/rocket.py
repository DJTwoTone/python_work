import pygame

class Rocket():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.xaxis = float(self.rect.centerx)
        self.yaxis = float(self.rect.bottom)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.xaxis += self.ai_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.xaxis -= self.ai_settings.rocket_speed_factor
        if self.moving_up and self.rect.bottom < self.screen_rect.bottom:
            self.yaxis += self.ai_settings.rocket_speed_factor
        if self.moving_down and self.rect.top > 0:
            self.yaxis -= self.ai_settings.rocket_speed_factor

        self.rect.centerx = self.xaxis
        self.rect.bottom = self.yaxis


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    