


"""

	GALACTICA DEMO

	This is a demo to test the game's GUI in Pygame
	using Pygame GUI.
"""



import sys
import random
import pygame_gui as gui
import pygame
from pygame.locals import *

SCREEN_X = 1024
SCREEN_Y = 576


# ========== Colours ===========
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0, 255, 0)
LGREY = (211, 211, 211)
SILVER = (192, 192, 192)
DGREY = (169, 169, 169)
GREY = (128, 128, 128)





class Game():
	def __init__(self):
		self.screen_obj = None
		self.clock = None

	def setup(self):
		self.screen_obj = pygame.display.set_mode( (SCREEN_X, SCREEN_Y) )
		self.clock = pygame.time.Clock()


class Surfaces():
	def __init__(self):
		# ___ IMAGES AND COLOURS ___
		self.bg = pygame.image.load('layout.png')
		
		# ___ INTERFACES AND GUI ___
		self.manager = gui.UIManager((SCREEN_X, SCREEN_Y))

		# GUI: Tabs
		tab_box_x = [45, 631]
		tab_box_y = [33, 64]
		tabs = 4
		tab_sep = (tab_box_x[1] - tab_box_x[0])/tabs


		self.tab_rect = []
		self.tab_text = ['Modules', 'Tools', 'Resources', 'Logs']
		self.tab_button = []

		for i in range(tabs):
			posx = tab_sep*i + tab_box_x[0]
			text = self.tab_text[i]

			_rect =  pygame.Rect((posx, tab_box_y[0]), (80, 30))
			_button = gui.elements.UIButton( _rect, 
					text = text, manager = self.manager)
			
			self.tab_rect.append( _rect )
			self.tab_button.append( _button )
		
		# Quit button
		quit_rect = pygame.Rect((SCREEN_X/2, SCREEN_Y/2), (80, 30)) 
		self.quit_button = gui.elements.UIButton(quit_rect,
							text = 'Quit', manager = self.manager)


	def draw(self, screen):
		#Backgrounds
		screen.blit(self.bg, (0,0))

		# ALL GUI
		self.manager.draw_ui(screen)






def draw_screen(game, surfaces):
	# Graphics and Interfaces
	surfaces.draw(game.screen_obj)
	
	pygame.display.update()



def main():

	# Initialise PyGame
	pygame.init()
	pygame.display.set_caption("Galactica - Demo")

	# Initialise classes
	game = Game()
	game.setup()
	surfaces = Surfaces()

	clock = pygame.time.Clock()
	run = True

	while (run):

		# Clock
		dt = clock.tick(100)/1000.0

		# Check events
		for event in pygame.event.get():
			# Quit check
			if event.type == pygame.QUIT:
				run = Fals
			# GUI check
			if event.type == pygame.USEREVENT:
				if event.ui_element == surfaces.quit_button:
					run = False

			surfaces.manager.process_events(event)

		if (run == False):
			break

		surfaces.manager.update(dt)
		
		# Keys
		keys = pygame.key.get_pressed() 
		if keys[pygame.K_SPACE]:
			run = False
		
		# Drawing
		draw_screen(game, surfaces)

	pygame.quit()


if __name__ == "__main__":
	main()