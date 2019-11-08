import sys
import pygame
from archering_settings import Settings
from archer import Archer
import archering_functions as arf
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("ARCHERING!!!")

    archer = Archer(ai_settings, screen)

    arrows = Group()

    while True:
        arf.check_events(ai_settings, screen, archer, arrows)
        archer.update()
        arf.update_arrows(arrows)
        arf.update_screen(ai_settings, screen, archer, arrows)

run_game()
