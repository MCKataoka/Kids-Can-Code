# Sprite Classes for platform game
#NEW STUFF 2
import pygame as pg
from settings import *
#NEW STUFF 6
vec = pg.math.Vector2

#NEW STUFF 3 THIS IS WHERE WE GOT TO!
class Player(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((30,40))
		self.image.fill(Yellow)
		self.rect = self.image.get_rect()
		#NEW STUFF 5 After this one make sure it works then explain how it doesnt move well
		self.rect.center = (width/2, height/2)
		# self.vx = 0
		# self.vy = 0
		#NEW STUFF 7 comment 2 lines above
		self.pos = vec(width/2, height/2)
		self.vel = vec(0,0)
		self.acc = vec(0,0)

	def update(self):
		# self.vx = 0
		#NEW STUFF 8 comment 2 lines above
		self.acc = vec(0,0)
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			# self.vx = -5
			#NEW STUFF 9 comment line above
			#self.acc.x = -5
			self.acc.x = -Player_acc
		if keys[pg.K_RIGHT]:
			# self.vx = 5
			#NEW STUFF 10 comment line above
			self.acc.x = Player_acc

		# self.rect.x += self.vx
		# self.rect.y += self.vy
		#NEW STUFF 11 comment 2 lines above
		#NEW STUFF 13
		self.acc += self.vel * player_friction
		#END OF NEW STUFF 13
		self.vel += self.acc
		self.pos += self.vel + 0.5 * self.acc
		#NEW STUFF 14 wrap the player around the sides of the screen
		if self.pos.x > width:
			self.pos.x = 0
		if self.pos.x < 0:
			self.pos.x = width



		self.rect.center = self.pos
