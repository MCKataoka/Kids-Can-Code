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
		#NEW STUFF 5
		self.font_name = pg.font.match_font(FONT_NAME)

	def new(self):
		# start a new game
		#NEW STUFF 7
		self.score = 0
		self.all_sprites = pg.sprite.Group()
		
		self.player = Player(self)
		self.all_sprites.add(self.player)
		
		self.platforms = pg.sprite.Group()
		
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
		
		#Check if player hits a platform - only if falling
		if self.player.vel.y > 0:
			hits = pg.sprite.spritecollide(self.player, self.platforms, False)
			if hits:
				self.player.pos.y = hits[0].rect.top + 1
				self.player.vel.y = 0.0
		 
		# if player reaches top 1/4 of the screen
		if self.player.rect.top <= height/4:
			self.player.pos.y += abs(self.player.vel.y)
			for plat in self.platforms:
				plat.rect.y += abs(self.player.vel.y)
				if plat.rect.top >= height:
					plat.kill()
					#NEW STUFF 8
					self.score += 10
		#NEW STUFF 3
		#Die!
		if self.player.rect.bottom > height:
			for sprite in self.all_sprites:
				sprite.rect.y -= max(self.player.vel.y, 10)
				if sprite.rect.bottom < 0:
					sprite.kill()

		if len(self.platforms) == 0
			self.playing = False

		# spawn new platforms to keep same average number
		while len(self.platforms) < 6:
			width2 = random.randrange(50,100)
			p = Platform(random.randrange(0,width-width2), random.randrange(-75,-30), width2, 20)
			self.platforms.add(p)
			self.all_sprites.add(p)

	def events(self):
		# Game Loop - events
		
		# Process input (events)
		for event in pg.event.get():
			# check for closing the window
			if event.type == pg.QUIT:
				
				if self.playing:
					self.playing = False
				self.running = False
			
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					self.player.jump()

	def draw(self):
		# Game Loop - draw
		
		self.screen.fill(Black)
		self.all_sprites.draw(self.screen)
		#NEW STUFF 9
		self.draw_text(str(self.score), 22, white, width/2, 15)
		# *after* drawing everything, flip the display
		pg.display.flip()

	def show_start_screen(self):
		# game splash/start screen
		pass

	def show_go_screen(self):
		# game over/continue
		pass
	#NEW STUFF 6
	def draw_text(self, text, size, color, x, y):
		font = pg.font.Font(self.font_name, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x,y)
		self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_go_screen()

pg.quit()
