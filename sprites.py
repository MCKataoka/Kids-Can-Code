# Sprite Classes for platform game

import pygame as pg
from settings import *

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
	def __init__(self):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((30,40))
		self.image.fill(Yellow)
		self.rect = self.image.get_rect()
		
		self.rect.center = (width/2, height/2)
		self.pos = vec(width/2, height/2)
		self.vel = vec(0,0)
		self.acc = vec(0,0)

	def update(self):
		#NEW STUFF 1 change the vector to 0.5
		self.acc = vec(0,0.5)
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			
			self.acc.x = -Player_acc
		if keys[pg.K_RIGHT]:
			
			self.acc.x = Player_acc

		
		#NEW STUFF 2 change so just the x direction is affected by friction
		self.acc.x += self.vel.x * player_friction
		
		self.vel += self.acc

		self.pos += self.vel + 0.5 * self.acc

		self.pos += self.acc
		
		if self.pos.x > width:
			self.pos.x = 0
		if self.pos.x < 0:
			self.pos.x = width


		#NEW STUFF 5 comment out line bellow and use following
		#self.rect.center = self.pos
		self.rect.midbottom = self.pos

#NEW STUFF 3
class Platform(pg.sprite.Sprite):
	def __init__(self, x, y, w, h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(Green)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
