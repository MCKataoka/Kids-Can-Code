# Pygamet template - skeleton for a new pygame project
import pygame
import random

width = 480
height = 600
fps = 60

# define colors
White = (255,255,255)
Red = (255,0,0)
Black = (0,0,0)
Green = (0,255,0)
Blue = (0,0,255)

# initialize pygame and create windon
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Platformer!")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
# Game loop
running = True
while running:
	#keep loop running at the right speed
	clock.tick(fps)
	# Process input (events)
	for event in pygame.event.get():
		# check for closing the window
		if event.type == pygame.QUIT:
			running = False

	# Update
	all_sprites.update()
    
	# Draw / render
	screen.fill(Black)
	all_sprites.draw(screen)
	# *after* drawing everything, flip the display
	pygame.display.flip()

pygame.quit()
