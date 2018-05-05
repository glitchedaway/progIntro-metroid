import pygame
walls = []
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

levelMap = [
    [LMap11, LMap12, LMap13]
    [LMap21, LMap22, LMap23]
    [LMap31, LMap32, LMap33]
LMap11 = [
    "NNNNNNNNNNNN"
    "W||||||||||W"
    "W|__||||__||"
    "W||||__||||X"
    "W|||_||_|||X"
    "W__||NN||__W"
    "W|||_NN_|||W"
    "W||||||||||W"
    "NNXXNNNNXXNN"
]
LMap12 = [
    "NNNNNNNNNNNN"
    "W||||||||||X"
    "W||||||||??X"
    "X|||||???||W"
    "X||???|||||W"
    "W__||||||||W"
    "W||_|||||||X"
    "W|||_||__||X"
    "NNNNXXXXNNNN"
]
LMap13 = [
    "NNNNNNNNNNNN"
    "X|||||||||ZW"
    "X||||||||||W"
    "WNNNNNNNNNNW"
    "W||||||||||W"
    "W||||||||||W"
    "X||||||||||W"
    "X||||||||||W"
    "NNNNXXXXNNNN"
]
LMap21 = [
    "NNNNNNNNNNNN"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "NNNNNNNNNNNN"
]
LMap22 = [
    "NNNNNNNNNNNN"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "NNNNNNNNNNNN"
]
LMap23 = [
    "NNNNNNNNNNNN"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "NNNNNNNNNNNN"
]
LMap31 = [
    "NNNNNNNNNNNN"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "NNNNNNNNNNNN"
]
LMap32 = [
    "NNNNNNNNNNNN"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "NNNNNNNNNNNN"
]
LMap33 = [
    "NNNNNNNNNNNN"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "W||||||||||W"
    "NNNNNNNNNNNN"
]
# turns the level string into actual level graphics - W = wall, E = exist. 
def createLevel(level):
    x = y = 0
    for row in level:
        for col in row:
            if col == "W":
                #white vertical line
                # for each column in the row (aka each character in each string in each list), put a wall there
            if col == "N":
                #make a white line there
                # ending rectangle is there.
            if col = "_"
                #make a red line there
            x += 16
        y += 16
        x = 0