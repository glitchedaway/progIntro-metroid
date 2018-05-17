import pygame
from platform import *
import settings
#rect collision source: https://www.pygame.org/project-Rect+Collision+Response-1061-.html
# player variable ideas taken from https://www.youtube.com/watch?v=7W0VKHzhCRQ
# i'm going to have a more or less rectangular hitbox until later on (because it's easier to code for),
# the purpose of this is to prevent corner catching (when your character stops on a corner b/c you move both x and y at once)
W, H = 720, 540
HW, HH = W / 2, H / 2
AREA = W * H
DS = pygame.display.set_mode((W,H))
class Player(object):
    def __init__(self, velocity, maxJumpRange):
        self.rect = pygame.Rect(20, 20, 8, 8)
        # sets how large the player's hitbox is. 
        # first two coords: top left point
        # second two coords: width & height of box
        self.velocity = velocity
        self.maxJumpRange = maxJumpRange
        self.prizeCheck = False 
    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.jumping = False
        self.jumpCounter = 0
        self.falling = True
    def keys(self):
        #if you press A or D you move left or right x pixels, equal to your velocity
        k = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a::
                    self.xVelocity = -self.velocity
                elif event.key == pygame.K_d:
                    self.xVelocity = self.velocity
        #if you press neither you don't move left/right
        else:
            self.xVelocity = 0

        #if you press W and you're not jumping already and you're not falling already, then you jump.
        if k[pygame.K_w] and not self.jumping and not self.falling:
            self.jumping = True
            self.jumpCounter = 0
    def move(self):
        self.x += self.xVelocity
        print("I moved to " + str(self.x) + ", "+ str(self.y))
        # readd collide check here eventually lol
        if self.jumping:
            self.y -= self.velocity
            self.jumpCounter += 1
            #if you hit your max jump range (defined above), then you're no longer jumping & you don't move up
            if self.jumpCounter == self.maxJumpRange:
                self.jumping = False
                self.falling = True
        elif self.falling:
            for wall in wallsFull:
                if self.rect.colliderect(wall.rect):
                    #tl;dr: if you were moving this way, you hit the opposite side of the wall. 
                    if self.xVelocity > 0:
                        self.rect.right = wall.rect.left
                    if self.xVelocity < 0:
                        self.rect.left = wall.rect.left
                    if self.jumping == True:
                        self.rect.bottom = wall.rect.top
                    if self.falling == True:
                        self.rect.top = wall.rect.bottom
            for wall in wallsPart:
                if self.rect.colliderect(wall.rect):
                    #however, to let you pass through platforms because collision is lame, you can press S to fall through flat platforms
                    if self.falling == True and not k[pygame.K_s]:
                        self.rect.top = wall.rect.bottom

            # if your next move would take you THROUGH the ground, it will instead move you up so that you won't and you are no longer falling.
            # if self.y <= H - 10 and self.velocity >= H - 10:
            #     self.y = H - 10
            #     self.falling = False
            else:
                self.y += self.velocity
    	#if you're inside the prize box, set the prize to true and respawn the level WITH the new platforms in place.
        if (self.rect.left >= 360 and self.rect.left <= 480) and (self.rect.top >= 1160 and self.rect.top <= 1320):
            self.prizeCheck = True
    def draw(self):
        # display = pygame.DS.get_surface()
        global DS
        pygame.draw.rect(DS, (255, 200, 0), self.rect)
        
    def do(self):
        self.keys()
        self.move()
        self.draw()
        