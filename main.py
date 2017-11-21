# Jumpy! - platform game.

import pygame as pg # so now you can just write pg.quit instead of pygame.quit()
import random

from settings import *

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
		#NEW STUFF 6 add self
		self.player = Player(self)
		self.all_sprites.add(self.player)
		
		self.platforms = pg.sprite.Group()
		#NEW STUFF 10 change how platforms are made
		#p1 = Platform(0, height-40, width, 40)
		for plat in platform_list:
			p = Platform(*plat)
			self.all_sprites.add(p)
			self.platforms.add(p)
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
		#NEW STUFF 8
		#Check if player hits a platform - only if falling
		if self.player.vel.y > 0:
			hits = pg.sprite.spritecollide(self.player, self.platforms, False)
			if hits:
				self.player.pos.y = hits[0].rect.top + 1
				self.player.vel.y = 0.0

	def events(self):
		# Game Loop - events
		
		# Process input (events)
		for event in pg.event.get():
			# check for closing the window
			if event.type == pg.QUIT:
				
				if self.playing:
					self.playing = False
				self.running = False
			#NEW STUFF 3
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					self.player.jump()

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
