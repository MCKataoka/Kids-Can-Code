# Sprite Classes for platform game

import pygame as pg
from settings import *

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
	#NEW STUFF 4 add game
	def __init__(self, game):
		pg.sprite.Sprite.__init__(self)
		#NEW STUFF 5
		self.game = game
		self.image = pg.Surface((30,40))
		self.image.fill(Yellow)
		self.rect = self.image.get_rect()
		
		self.rect.center = (width/2, height/2)
		self.pos = vec(width/2, height/2)
		self.vel = vec(0,0)
		self.acc = vec(0,0)
	#NEW STUFF 7
	def jump(self):
		#jump only if stading on a platform
		# new stuff 5
		self.rect.x += 1
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.x -=1
		if hits:
			self.vel.y = -20


	def update(self):
		#NEW STUFF 2 Change the acc vector
		self.acc = vec(0,player_grav)
		keys = pg.key.get_pressed()
		if keys[pg.K_LEFT]:
			
			self.acc.x = -Player_acc
		if keys[pg.K_RIGHT]:
			
			self.acc.x = Player_acc

		
		
		self.acc.x += self.vel.x * player_friction
		
		self.vel += self.acc

		self.pos += self.vel + 0.5 * self.acc

		self.pos += self.acc
		
		if self.pos.x > width:
			self.pos.x = 0
		if self.pos.x < 0:
			self.pos.x = width


		
		#self.rect.center = self.pos
		self.rect.midbottom = self.pos


class Platform(pg.sprite.Sprite):
	def __init__(self, x, y, w, h):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface((w,h))
		self.image.fill(Green)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
