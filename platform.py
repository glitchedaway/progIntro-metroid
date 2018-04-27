import math, random, sys
import pygame
from pygame.locals import *

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# colors so they don't have to be repeated
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

platform_y = H - 50


collision_map = pygame.Surface((W, H))
HIT = WHITE
MISS = BLACK
pygame.draw.line(collision_map, WHITE, (0, platform_y), (W, platform_y), 1)


player_x = HW
player_y = 0
falling_velocity = 3

# main loop
while True:
	events()

    #if you're going to fall into a platform then you are on the platform
	if player_y <= platform_y and player_y + falling_velocity >= platform_y:
		player_y = platform_y
	else:
    #otherwise you fall as normal
		player_y += falling_velocity
		

	collision = False
    #if you hit a white line you have hit the platform
    #otherwise you didn't and you keep falling
	for collision_y in range(player_y, player_y + falling_velocity):
		color = collision_map.get_at((player_x, collision_y))
		if color == HIT:
			collision = True
			player_y = collision_y
			break
	if not collision:
		player_y += falling_velocity

    #draw the player as a circle
	pygame.draw.circle(DS, WHITE, (player_x, player_y - 25), 25, 0)
    #draw platforms as lines
	pygame.draw.line(DS, WHITE, (0, platform_y), (W, platform_y), 1)
	#update screen
	pygame.display.update()