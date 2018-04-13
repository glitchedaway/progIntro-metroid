#week two

import os
from random import *
import pygame
from pygame import *


#collision source: https://www.pygame.org/project-Rect+Collision+Response-1061-.html
# i'm going to have a more or less rectangular hitbox until later on (because it's easier to code for),
# the purpose of this is to prevent corner catching (when your character stops on a corner b/c you move both x and y at once)
class Player(object):
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)
        # sets how large the player's hitbox is. 
        # first two coords: top left point
        # second two coords: width & height of box
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # move each axis separately to prevent corner catching
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        for wall in walls:
            if self.rect.colliderect(wall.rect):
                #if you collide with a wall:
                if dx > 0: # If you were moving right:
                    self.rect.right = wall.rect.left
                    #then you hit the left side of the wall
                if dx < 0: # If you were moving left
                    self.rect.left = wall.rect.right
                    # then you hit the right side of the wall
                if dy > 0: # If you were moving up:
                    self.rect.bottom = wall.rect.top
                    # then you hit the bottom side of the wall
                if dy < 0: # If you were moving down
                    self.rect.top = wall.rect.bottom
                    # then you hit the top side of the wall 
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

#start pygame with window centered
# Surface fill fix (because they changed screen.fill or something - it's not working atm so workarounds ho): https://stackoverflow.com/questions/41873581/pygame-surface-fill-not-working

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
size = [640, 480]
screen = pygame.display.set_mode(size)
player = Player()


# general defined variables
clock = pygame.time.Clock()
walls = [] # list to hold the player later on - aka position of walls

# holds the level layout as a list of strings row by row
level = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W         WWWWWW   W",
    "W   WWWW       W   W",
    "W   W        WWWW  W",
    "W WWW  WWWW        W",
    "W   W     W W      W",
    "W   W     W   WWW WW",
    "W   WWW WWW   W W  W",
    "W     W   W   W W  W",
    "WWW   W   WWWWW W  W",
    "W W      WW        W",
    "W W   WWWW   WWW   W",
    "W     W    E   W   W",
    "WWWWWWWWWWWWWWWWWWWW",
]
screenDrawn = False
# turns the level string into actual level graphics - W = wall, E = exist. 
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
            # for each column in the row (aka each character in each string in each list), put a wall there
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
            # ending rectangle is there.
        x += 16
    y += 16
    x = 0

running = True
while running:
    clock.tick(60) 
    for e in pygame.event.get():    
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
        # close the game if escape or the x is hit
    
    # move the player either 
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    #draw the screen
    if screenDrawn = False:
        screen.fill((0,0,0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
            pygame.draw.rect(screen, (255, 0, 0), end_rect)
            pygame.draw.rect(screen, (255, 200, 0), player.rect)
            pygame.display.flip()
        screenDrawn = True

