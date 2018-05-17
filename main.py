#week two

import os
from random import *
import pygame
from pygame import *
from player import *
from settings import *
from platform import *

pygame.init()
W, H = 720, 540
HW, HH = W / 2, H / 2
AREA = W * H
DS = pygame.display.set_mode((W,H))

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()


# general defined variables
clock = pygame.time.Clock()
P = Player(3, 80)
P.setLocation(120, 80)
# pRed = platforms(flatP)
# pWhite = platforms(solidP)
# pBlue = platforms(prizeP)
createLevel()
running = True
prize = False
LSpawn = False
events()
while running:
	DS.fill(0)
	#if you hit the blue box, set your position below it, spawn in the boxes at the top, move down.
	if P.prizeCheck == True and prize == False:
		prize = True
		createLevel()
		P.setLocation(1240, 480)
	#draw all the walls
	for wall in wallsPart:
		pygame.draw.rect(DS, (255, 255, 255), wall.rect)
	for wall in wallsFull:
		pygame.draw.rect(DS, (255, 255, 255), wall.rect)
	pygame.draw.rect(DS, (255, 200, 0), P.rect)
	events()
	P.do()
	#flip your screen
	pygame.display.flip()
