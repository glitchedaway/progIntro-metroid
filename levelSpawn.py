import pygame
walls = []
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

levelA = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "W                  W",
    "WWWWWWWWWWWWWWWWWWWW",

]
# turns the level string into actual level graphics - W = wall, E = exist. 
def createLevel(level):
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