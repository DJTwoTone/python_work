import sys
import pygame
from sheriff_badge import Badge

def run_game():
	
	pygame.init
	screen = pygame.display.set_mode((400, 400))
	pygame.display.set_caption("Blue Screen")
	bg_color = (3, 119, 252)
	
	badge = Badge(screen)
	
	while True:
		screen.fill(bg_color)
		badge.blitme()
		pygame.display.flip()
		
		
run_game()
