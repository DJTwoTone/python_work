import sys
import pygame
from starfield_settings import Settings
from star import Star
import field_functions as f_f
from pygame.sprite import Group


def run_game():
    pygame.init
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Starry Starry Field")

    stars = Group()

    f_f.create_field(ai_settings, screen, stars)

    while True:
        f_f.check_events(ai_settings, screen)
        f_f.update_screen(ai_settings, screen, stars)


run_game()