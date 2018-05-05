#week two

import os
from random import *
import pygame
from pygame import *
from player import *
from levelSpawn import *

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface			
W, H = 480, 360
HW, HH = W / 2, H / 2
AREA = W * H


# general defined variables
clock = pygame.time.Clock()
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
# turns the level string into actual level graphics - W = wall, E = exist. 
createLevel(levelA)
platRed  = platforms(RED)
platWhite = platforms(WHITE)
P = player()
running = True
while running:
    clock.tick(60) 
    for e in pygame.event.get():    
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
    events()
	redP = True
	platRed.do(P)
	redP = False
	platWhite.do(P)
	P.do()
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)
    pygame.display.flip()   