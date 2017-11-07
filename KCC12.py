# Pygamet template - skeleton for a new pygame project 

# WE ARE GOING TO START WORK TOWARDS A SCHMUP (Shoot them up)

# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3 <http://creativecommons.org/licenses/by/3.0/>

# Art from Kenny.nl

import pygame
import random
import os

from os import path
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')


width = 480

height = 600

fps = 60

POWERUP_TIME = 5000


# define colors

White = (255,255,255)
Red = (255,0,0)
Black = (0,0,0)
Green = (0,255,0)
Blue = (0,0,255)

# Set up assests folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"Schump")




# initialize pygame and create windon
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Am!")
clock = pygame.time.Clock()





font_name = pygame.font.match_font("arial")


def draw_text(surf, text, size, x, y):
	
	font = pygame.font.Font(font_name, size)
	#True makes the font anti-aliased this makes it nice and smooth.
	text_surface =  font.render(text, True, White)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x,y)
	surf.blit(text_surface, text_rect)

def newmob():

	m = Mob()
	all_sprites.add(m)
	mobs.add(m)

def draw_shield_bar(surf, x,y,pct):
	#Prevents the bar to go into the negatives
	if pct < 0:
		pct = 0
	BAR_LENGTH = 100
	BAR_HEIGHT = 10
	fill = (pct/100)*BAR_LENGTH
	outline_rect = pygame.Rect(x,y,BAR_LENGTH, BAR_HEIGHT)
	fill_rect = pygame.Rect(x,y, fill, BAR_HEIGHT)
	pygame.draw.rect(surf, Green, fill_rect)
	pygame.draw.rect(surf,White, outline_rect, 1)

def draw_lives(surf, x,y,lives,img):
	#Prevents the bar to go into the negatives
	for i in range(lives):
		img_rect = img.get_rect()
		img_rect.x = x + 30* i
		img_rect.y = y
		surf.blit(img,img_rect)

class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.transform.scale(player_img, (50,38))
		#removes the black in the back
		self.image.set_colorkey(Black)
		
		# self.image.fill(Green)
		self.rect = self.image.get_rect()
		
		self.radius = 20
		
		self.rect.centerx = width/2
		self.rect.bottom = height - 10
		self.speedx = 0
		self.shield = 100
		
		# We are adding an autoshoot function. So we dont constantly have to press the space bar
		self.shoot_delay = 250
		self.last_shot = pygame.time.get_ticks()
		
		self.lives = 3
		self.hidden = False
		self.hide_timer = pygame.time.get_ticks()
		
		self.power = 1
		self.power_time = pygame.time.get_ticks()

	def update(self):
		
		if self.power >=2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
			self.power -=  1
			self.power_time = pygame.time.get_ticks()
		#unhide if hidden
		if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
			self.hidden = False
			self.rect.centerx = width/2
			self.rect.bottom = height-10

		self.speedx = 0
		keystate = pygame.key.get_pressed()

		if keystate[pygame.K_LEFT]:
			self.speedx = -5
		if keystate[pygame.K_RIGHT]:
			self.speedx = 5
		
		if keystate[pygame.K_SPACE]:
			self.shoot()

		self.rect.x += self.speedx 

		if self.rect.right > width:
			self.rect.right = width
		if self.rect.left < 0:
			self.rect.left = 0

	

	def powerup(self):
		self.power += 1
		self.power_time = pygame.time.get_ticks()
			
	def shoot(self):
		
		now = pygame.time.get_ticks()
		if now - self.last_shot > self.shoot_delay:
			self.last_shot = now
			
			if self.power == 1:
				bullet = Bullet(self.rect.centerx, self.rect.top)
				all_sprites.add(bullet)
				bullets.add(bullet)
				shoot_sound.play()
			
			if self.power >= 2:
				bullet1 = Bullet(self.rect.left, self.rect.centery)
				bullet2 = Bullet(self.rect.right, self.rect.centery)
				all_sprites.add(bullet1)
				all_sprites.add(bullet2)
				bullets.add(bullet1)
				bullets.add(bullet2)
				shoot_sound.play()

	
	def hide(self):

		# hide the player temporarily
		self.hidden = True
		self.hide_timer = pygame.time.get_ticks()
		self.rect.center = (width/2, height+200)
		
		

class Mob(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		# self.image = pygame.Surface((30,40))
		# self.image.fill(Red)

		
		self.image_original = random.choice(meteor_images)
		#removes the black in the back
		self.image_original.set_colorkey(Black)

		
		self.image = self.image_original.copy()
		
		self.rect = self.image.get_rect()

		
		self.radius = int(self.rect.width * .85 / 2)
		

		#pygame.draw.circle(self.image, Red, self.rect.center, self.radius)

		self.rect.x = random.randrange(0, width - self.rect.width)	#if you leave out 0 oygame assumes it is 0
		
		self.rect.y = random.randrange(-250, -200)	
		self.speedy = random.randrange(1,8)
		
		self.speedx = random.randrange(-3,3)

		
		self.rot = 0
		self.rot_speed = random.randrange(-8,8)
		# how many tick of the clock since the game has started
		self.last_update = pygame.time.get_ticks()


		
	def rotate(self):
		now = pygame.time.get_ticks()

		# This is checking how long it has been since the last time that we updated.
			# by calculating the ticks since the last time until now
		if now - self.last_update > 50:
			self.last_update = now

			
			# we are rotating first from 0-1 then 0-2 then 0-3 until we got from 0-360
				#the reason we do it like that is so that it doesnt glitch so the will just 
				# appear on the screen already rotated
			self.rot = (self.rot + self.rot_speed) % 360
			# USE THIS UNTIL STEP 6 self.image = pygame.transform.rotate(self.image_original, self.rot)

		
			new_image = pygame.transform.rotate(self.image_original, self.rot)
			old_center = self.rect.center
			self.image = new_image
			self.rect = self.image.get_rect()
			self.rect.center = old_center

			# This is the version that crashes it! Have him do it
			#self.image = pygame.transform.rotate(self.image, self.rot_speed)



	def update(self):
		
		self.rotate()
		
		self.rect.x += self.speedx
		
		self.rect.y += self.speedy

        
		if self.rect.top > height + 10 or self.rect.left < -25 or self.rect.right > width + 20:
			self.rect.x = random.randrange(0, width - self.rect.width)	#if you leave out 0 oygame assumes it is 0
			self.rect.y = random.randrange(-100, -40)	
			self.speedy = random.randrange(1,8)


class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		# self.image = pygame.Surface((10,20))
		# self.image.fill(White)

		
		self.image = bullet_img
		#removes the black in the back
		self.image.set_colorkey(Black)
		self.rect = self.image.get_rect()
		# we need the bullet to span where the player is.
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -10


	def update(self):
		
		
		self.rect.y += self.speedy
		# kill if it moves off the top of the screen
		if self.rect.bottom < 0:
			self.kill()



class Pow(pygame.sprite.Sprite):
	
	def __init__(self, center):
		pygame.sprite.Sprite.__init__(self)
		
		self.type = random.choice(['shield','gun'])		
		
		self.image = powerup_images[self.type]
		#removes the black in the back
		self.image.set_colorkey(Black)
		self.rect = self.image.get_rect()
		
		self.rect.center = center
		
		self.speedy = 4


	def update(self):
		self.rect.y += self.speedy
		
		if self.rect.top > height:
			self.kill()

class Explosion(pygame.sprite.Sprite):
	def __init__(self, center, size):
		pygame.sprite.Sprite.__init__(self)
		self.size = size
		self.image = explosion_anim[self.size][0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		
		self.frame_rate = 75

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame +=  1
			if self.frame == len(explosion_anim[self.size]):
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_anim[self.size][self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

# NEW STFF 5

def show_go_screen():
	# NEW STFF 6 this next might not work for him so make sure the part before adding the backgroung works
	screen.blit(background, background_rect)
	draw_text(screen, "SHMUP!", 64, width/2, height/4)
	draw_text(screen, "Arrow keys move, Space to fire", 22, width/2, height/2)
	draw_text(scree, "Press a key to begin", 18, width/2, height*3/4)
	pygame.display.flip()
	waiting = True
	while waiting:
		cloc.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				waiting == False


# Load all game graphics



background = pygame.image.load(path.join(img_dir, "bHiPMju.png")).convert()
background_rect = background.get_rect()


player_img = pygame.image.load(path.join(img_dir,"playerShip2_green.png")).convert()

player_mini_img = pygame.transform.scale(player_img,(25,19))
player_mini_img.set_colorkey(Black)
bullet_img = pygame.image.load(path.join(img_dir,"laserBlue16.png")).convert()


meteor_images = []
meteor_list = ['meteorGrey_big1.png', 'meteorGrey_big2.png', 'meteorGrey_big3.png',
				'meteorGrey_big4.png', 'meteorGrey_med1.png', 'meteorGrey_med2.png',
				'meteorGrey_small1.png', 'meteorGrey_small2.png', 'meteorGrey_tiny1.png',
				'meteorGrey_tiny2.png']

for img in meteor_list:
	meteor_images.append(pygame.image.load(path.join(img_dir,img)).convert())


explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []

explosion_anim['player'] = []

for i in range(9):
	filename = 'regularExplosion0{}.png'.format(i)
	img = pygame.image.load(path.join(img_dir, filename)).convert()
	img.set_colorkey(Black)
	img_lg = pygame.transform.scale(img, (75,75))
	explosion_anim['lg'].append(img_lg)
	img_sm = pygame.transform.scale(img, (32,32))
	explosion_anim['sm'].append(img_sm)
	
	filename = 'sonicExplosion0{}.png'.format(i)
	img = pygame.image.load(path.join(img_dir, filename)).convert()
	img.set_colorkey(Black)
	explosion_anim['player'].append(img)


powerup_images = {}
powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()

# Load all the game sounds
shoot_sound = pygame.mixer.Sound(path.join(snd_dir,'Laser_Shoot6.wav'))


#shield_sound = pygame.mixer.Sound(path.join(snd_dir,'pow4.wav'))
#power_sound = pygame.mixer.Sound(path.join(snd_dir,'pow5.wav'))



explosion_sounds = []
explosions = ['Explosion17.wav', 'Explosion4.wav']

for sd in explosions:
	explosion_sounds.append(pygame.mixer.Sound(path.join(snd_dir,sd)))


#player_die_sound = pygame.mixer.Sound(path.join(snd_dir, 'rumble1.ogg'))


# pygame.mixer.music.load(path.join(snd_dir,'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
# pygame.mixer.music.set_volume(0.4)

# all_sprites = pygame.sprite.Group() 

# mobs = pygame.sprite.Group()

# bullets = pygame.sprite.Group()

# powerups = pygame.sprite.Group()

# player = Player()
# all_sprites.add(player)

# for i in range(8):
	
# 	newmob()

# score = 0


#pygame.mixer.music.play(loops=-1)

# Game loop

#NEW STUFF 1
game_over = True
running = True
while running:
	#NEW STUFF 2
	if game_over:

		show_go_screen()
		game_over = False
		#NEW STUFF 3 - Cut and pasted from the section just above
		all_sprites = pygame.sprite.Group() 
		mobs = pygame.sprite.Group()
		bullets = pygame.sprite.Group()
		powerups = pygame.sprite.Group()
		player = Player()
		all_sprites.add(player)
		for i in range(8):
			newmob()
		score = 0


	#keep loop running at the right speed
	clock.tick(fps)
	# Process input (events)
	for event in pygame.event.get():
		# check for closing the window

		if event.type == pygame.QUIT:
			running = False


	# Update
	all_sprites.update()

	
	hits = pygame.sprite.groupcollide(mobs,bullets,True,True)


	for hit in hits:
		
		score += 50 - hit.radius
		random.choice(explosion_sounds).play()
		expl = Explosion(hit.rect.center, 'lg')
		all_sprites.add(expl)
		
		if random.random() > .9:
			pow = Pow(hit.rect.center)
			all_sprites.add(pow)
			powerups.add(pow)
		newmob()



	#Change it so now when you get hit with the mob you will actually stay alive
		# and you will only die till the shield has gone away
	# check to see if a mob hit the player
	hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
		#if statement hits is false if it is empty
	for hit in hits:
		player.shield -= hit.radius * 2
		expl = Explosion(hit.rect.center, 'sm')
		all_sprites.add(expl)
		# we need to spawn a new mob to replace it now that the game doesnt end.
		newmob()
		if player.shield <= 0:
			
			#player_die_sound.play()
			
			death_explosion = Explosion(player.rect.center, 'player')
			all_sprites.add(death_explosion) #pause here and have him try it
			
			#running = False ONLY AFTER TRYING IT OUT FIRST

			
			player.hide()
			player.lives -= 1
			player.shield = 100

	
	hits = pygame.sprite.spritecollide(player, powerups, True)
	for hit in hits:
		if hit.type == 'shield':
			player.shield += random.randrange(10,20)
			
			#shield_sound.play()
			if player.shield >= 100:
				player.shield =100
		
		if hit.type == 'gun':
			player.powerup()
			
			#power_sound.play()

		
	# if the player died and the explosion has finished playing
	# if not player.alive() and not death_explosion.alive():
	
	
	if player.lives == 0 and not death_explosion.alive():
		# NEW STUFF 4
		game_over = True
		# running = False

	# Draw / render
	screen.fill(Black)
	
	screen.blit(background, background_rect)
	all_sprites.draw(screen)

	
	draw_text(screen, str(score), 18, width/2, 10)
	
	draw_shield_bar(screen, 5,5,player.shield)
	
	draw_lives(screen, width-100,5,player.lives, player_mini_img)
	# *after* drawing everything, flip the display
	pygame.display.flip()

pygame.quit()
