# Pygamet template - skeleton for a new pygame project
#NEW STUFF 4 move the imports to a main.py file
import pygame
import random
#NEW STUFF 2 (you can just import but then you would have to do things like settings.width)
from settings import *

#NEW STUFF 1 move these and save them in a new file named settings
# width = 480
# height = 600
# fps = 60

# # define colors
# White = (255,255,255)
# Red = (255,0,0)
# Black = (0,0,0)
# Green = (0,255,0)
# Blue = (0,0,255)

#NEW STUFF 8 Move to the main.py
# initialize pygame and create windon
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((width,height))
# #NEW STUFF 3 remove the old title and create a variable in the settings folder
# pygame.display.set_caption(title)
# clock = pygame.time.Clock()

#NEW STUFF 10 Move to the main.py
# all_sprites = pygame.sprite.Group()


# Game loop
running = True
while running:
	#keep loop running at the right speed
	clock.tick(fps)
	#NEW STUFF 13 Move to the main.py
	# Process input (events)
	# for event in pygame.event.get():
	# 	# check for closing the window
	# 	if event.type == pygame.QUIT:
	# 		running = False

	# Update
	#NEW STUFF 16 Move to the main.py
	all_sprites.update()
    
	# Draw / render
	#NEW STUFF 18 Move to the main.py
	# screen.fill(Black)
	# all_sprites.draw(screen)
	# # *after* drawing everything, flip the display
	# pygame.display.flip()

pygame.quit()
