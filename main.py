# Jumpy! - platform game.

import pygame as pg # so now you can just write pg.quit instead of pygame.quit()
import random

from settings import *
#NEW STUFF 1
from sprites import *



class Game:
	def __init__(self):
		
		# initialize game window, etc
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((width,height))
		pg.display.set_caption(title)
		self.clock = pg.time.Clock()
		self.running = True

	def new(self):
		# start a new game
		
		self.all_sprites = pg.sprite.Group()
		#NEW STUFF 4
		self.player = Player()
		self.all_sprites.add(self.player)
		self.run()
	

	def run(self):
		#Game Loop 
		
		self.playing = True
		while self.playing:
			self.clock.tick(fps)
			self.events()
			self.update()
			self.draw()

	def update(self):
		# Game Loop - Update
		
		self.all_sprites.update()

	def events(self):
		# Game Loop - events
		
		# Process input (events)
		for event in pg.event.get():
			# check for closing the window
			if event.type == pg.QUIT:
				
				if self.playing:
					self.playing = False
				self.running = False

	def draw(self):
		# Game Loop - draw
		
		self.screen.fill(Black)
		self.all_sprites.draw(self.screen)
		# *after* drawing everything, flip the display
		pg.display.flip()

	def show_start_screen(self):
		# game splash/start screen
		pass

	def show_go_screen(self):
		# game over/continue
		pass


g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_go_screen()

pg.quit()
