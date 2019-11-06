import sys
import pygame
from rocket_settings import Settings
from rocket import Rocket
import rocket_functions as rf

def run_game():

    pygame.init
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("ROCKETING!!!!")

    rocket = Rocket(ai_settings, screen)

    while True:
        rf.check_events(rocket)
        rocket.update()ls
        rf.update_screen(ai_settings, screen, rocket)

run_game()