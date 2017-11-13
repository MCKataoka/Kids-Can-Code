# Jumpy! - platform game.
# NEW STUFF 7
import pygame as pg # so now you can just write pg.quit instead of pygame.quit()
import random
#NEW STUFF 2 (you can just import but then you would have to do things like settings.width)
from settings import *


#NEW STUFF 5
class Game:
	def __init__(self):
		# NEW STUFF 9 make sure its all pg
		# initialize game window, etc
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((width,height))
		pg.display.set_caption(title)
		self.clock = pg.time.Clock()
		self.running = True

	def new(self):
		# start a new game
		# NEW STUFF 11 make sure its all pg
		all_sprites = pg.sprite.Group()
		#NEW STUFF 20
		self.run()
		#END OF NEW STUFF 20

	def run(self):
		#Game Loop 
		#NEW STUFF 12 
		self.playing = True
		while self.playing:
			self.clock.tick(fps)
			self.events()
			self.update()
			self.draw()

	def update(self):
		# Game Loop - Update
		#NEW STUFF 17
		self.all_sprites.update()

	def events(self):
		# Game Loop - events
		#NEW STUFF 14 Dont forget the pg!
		# Process input (events)
		for event in pg.event.get():
			# check for closing the window
			if event.type == pg.QUIT:
				#NEW STUFF 1516
				if self.playing:
					self.playing = False
				self.running = False

	def draw(self):
		# Game Loop - draw
		#NEW STUFF 19 dont forget selfs
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

# NEW STUFF 6
g = Game()
g.show_start_screen()
while g.running():
	g.new()
	g.show_go_screen()

pg.quit()
