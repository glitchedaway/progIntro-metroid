#week two

import os
from random import *
import pygame
from pygame import *
from player import *
from levelSpawn import *

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
size = [640, 480]
screen = pygame.display.set_mode(size)
player = Player()


# general defined variables
clock = pygame.time.Clock()

# turns the level string into actual level graphics - W = wall, E = exist. 
createLevel(levelA)

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
        player.move(-1, 0)
        print("Player moved left")
    if key[pygame.K_RIGHT]:
        player.move(1, 0)
        print("Player moved right")
    if key[pygame.K_UP]:
        playerJump()
        print("Player jumped")
    if key[pygame.K_DOWN]:
        player.move(0, 1)
        print("Player moved down")
    #draw the screen
    screen.fill((255,255,255))
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 0), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.display.flip()