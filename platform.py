import math, random, sys
import pygame
from pygame.locals import *
import player 
# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
class platform:
	def __init__(self, x, y, width):
		self.x1 = x
		self.y = y
		self.x2 = x + width
		self.redP = True
	def test(self, player):
	    # the player is left of a platform's left edge or right of a platform's right edge: he doesn't collide
		if player.x < self.x1 or player.x > self.x2: return None
		#however, if it's hitting the top and he's moving down towards the 
		if player.y <= self.y and player.y + player.velocity >= self.y: return self
		return None
		
class platforms:
	def __init__(self):
		self.container = list([])
	
	def add(self, p):
		self.container.append(p)
		
	def testCollision(self, player):
		if not player.falling: return False
		for p in self.container:
			result = p.test(player)
			if result:
				player.currentPlatform = result
				player.y = result.y
				player.falling = False
				return True
		return False
		
	def draw(self):
		global WHITE, RED
		display = pygame.display.get_surface()
		for p in self.container:
			if redP = True:
				pygame.draw.line(display, RED, (p.x1, p.y), (p.x2, p.y), 1)
			else:
				pygame.draw.line(display, WHITE, (p.x1, p.y), (p.x2, p.y), 1
	def do(self, player):
		self.testCollision(player)
		self.draw()



