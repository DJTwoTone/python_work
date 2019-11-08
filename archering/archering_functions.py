import sys
import pygame
from arrow import Arrow

def check_events(ai_settings, screen, archer, arrows):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, archer, arrows)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, archer)

def check_keydown_events(event, ai_settings, screen, archer, arrows):
    if event.key == pygame.K_UP:
        archer.moving_up = True
    elif event.key == pygame.K_DOWN:
        archer.moving_down = True
    elif event.key == pygame.K_SPACE:
        shoot_arrow(ai_settings, screen, archer, arrows)

def shoot_arrow(ai_settings, screen, archer, arrows):
    if len(arrows) < ai_settings.arrows_allowed:
        new_arrow = Arrow(ai_settings, screen, archer)
        arrows.add(new_arrow)

def check_keyup_events(event, archer):
    if event.key == pygame.K_UP:
        archer.moving_up = False
    elif event.key == pygame.K_DOWN:
        archer.moving_down = False

def update_arrows(arrows):
    arrows.update()

    for arrow in arrows.copy():
        if arrow.rect.left <= 0:
            arrows.remove(arrow)
    print(len(arrows))

def update_screen(ai_settings, screen, archer, arrows):
    screen.fill(ai_settings.bg_color)

    for arrow in arrows.sprites():
        arrow.draw_arrow()

    archer.blitme()

    pygame.display.flip()