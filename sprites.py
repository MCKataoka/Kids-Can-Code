# Sprite Classes for platform game

import pygame as pg
from settings import *

vec = pg.math.Vector2


class Player(pg.sprite.Sprite):
	
	def __init__(self, game):
		pg.sprite.Sprite.__init__(self)
		
		self.game = game
		self.image = pg.Surface((30,40))
		self.image.fill(Yellow)
		self.rect = self.image.get_rect()
		
		self.rect.center = (width/2, height/2)
		self.pos = vec(width/2, height/2)
		self.vel = vec(0,0)
		self.acc = vec(0,0)

	def jump(self):
		#jump only if stading on a platform
		
		self.rect.x += 1
		hits = pg.sprite.spritecollide(self, self.game.platforms, False)
		self.rect.x -=1
		if hits:
			#NEW STUFF 2 change to variable player_jump
			self.vel.y = -Player_Jump


	def update(self):
		
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
