import math, random, sys
import pygame
from pygame.locals import *
import player 
import settings

BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
BLUE = (0, 0, 255, 255)
wallsFull = []
wallsPart = []
class WallFull(object):
    def __init__(self, pos):
        wallsFull.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 20, 20)
class WallPlat(object):
    def __init__(self, pos):
        wallsPart.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 20, 1)
# # the following is taken from 
# class platforms:
#     def __init__(self, platType):
#         self.container = list([])
#         self.platType = platType
#     def add(self, p):
#         self.container.append(p)
#     def testCollision(self, player):
#         if not player.falling: 
#             return False
#         for p in self.container:
#             result = p.test(player)
#             if result:
#                 player.currentPlatform = result
#                 player.y = result.y
#                 player.falling = False
#         return True
#     def draw(self, platType, mod, stat):
#         global WHITE
#         display = pygame.display.get_surface()
#         for p in self.container:
#             if self.platType == "flatP":
#                 pygame.draw.line(display, RED, (p.x1, p.y), (p.x2, p.y), 1)
#             if self.platType == "prizeP":
#                 pygame.draw.line(display, BLUE, (p.x1, p.y), (p.x2, p.y), 40)
#     def do(self, player):
#         self.testCollision(player)
#         self.draw()
"""
general outline:
(each mini-section can be viewed as being sectioned off by
 two two-wide walls that extend a good distance. Player progression is as such:
11 => 12 => 13
||
21 <> 22    23
^^    VV    ^V
31 <> 32 <> 33
"""

LMapComb = [
    "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
    "N||||||||||NN||||||||||||||||||||||N"
    "N|__||||__|NN||||||||_||||||||||||ZN"
    "N||||__||||NN|||||___|NNNNNNNNNNNNNN"
    "N||||__||||NN|||_|||||NN|||||||||||N"
    "N|||_NN_|||NN__|||||||NN||__|||__||N"
    "N|||_NN_|||NN||__|||||||||_||||||_|N"
    "N||_|NN|_|_NN||||__|||||||__|||__||N"
    "NN_|NNNN|_NNNNNNNNNNNNNNNNNNN_|NNNNN"
    "NN|_NNNN_|NNNNNNNNNNNNNNNNNNN|_NNNNN"
    "N|__||||__|NN||||||||||NN||||_|||||N"
    "N||||__||||NN_NNNNNNN||NN|||____|||N"
    "NNNN||||NNNNN|N||||||||NN__||||||||N"
    "N|||N__||||NN_N||_|_|NNNN|||__|__||N"
    "N|||N__||_|NN|N_|||||||NN|||||||||_N"
    "N_|||||_|||||_N|__||__|NN|||||||__|N"
    "N||__|_|||||||N_||||||_NN||||__||||N"
    "NNNNNNNNN__NNNNNN||||NNNNNNNNNNNN|_N"
    "NNNNNNNNN__NNNNNN||||NNNNNNNNNNNN_|N"
    "N||||||____NN|||____||_NN|||||N|||_N"
    "N||||__||||NN|_||||||_|NN|_N||N|__|N"
    "N||__||||||NN_|||||||||NN||N|_N_|||N"
    "N__|||NNNNNNN|_|||NNNNNNN|_N||N||_|N"
    "N|||_||||||||_|||||||_|||||N_|N|||_N"
    "N||_||||||||||_|||||_|||||_N||N|_||N"
    "N|||||||||NNN_||_N|N||NNNN|N|_|||||N"
    "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN"
]
# pRed = platforms("flatP")
# pWhite = platforms("solidP")
# pBlue = platforms("prizeP")
def createLevel():
    LSpawn = False
    #https://www.pygame.org/project-Rect+Collision+Response-1061-.html concept from here, edits made as necessary to work with game mapd
    rY = cX = 0
    global LMapComb
    for row in LMapComb:
        #for each line in the map, track where we are, as well as resetting the column tracker
        for col in row:
            #turns each character in the map into a character.
            if col == "N":
                WallFull((cX, rY))
            if col == "_":
                WallPlat((cX, rY))
            print("plat spawned at " + str(cX) + ", " + str(rY))
            cX += 40
            #if your next platform would be off screen, new line of platforms.
            if cX >= 720:
                cX = 0
                rY += 20
        rY + 20
        cX = 0
    LSpawn = True

            # if col == "_":
            #     pRed.add(platform(40*rowC, 40*colC, 40))
            # if col == "?" and prize == True:
            #     pRed.add(platform(40*rowC, 40*colC, 40))
            # if col == "~":
            #     pBlue.add(platform(40*rowC, 40*colC, 40))
                