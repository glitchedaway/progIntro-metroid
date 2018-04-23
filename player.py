import pygame
#collision source: https://www.pygame.org/project-Rect+Collision+Response-1061-.html
# player variable ideas taken from https://www.youtube.com/watch?v=7W0VKHzhCRQ
# i'm going to have a more or less rectangular hitbox until later on (because it's easier to code for),
# the purpose of this is to prevent corner catching (when your character stops on a corner b/c you move both x and y at once)

class Player(object):
    def __init__(self, velocity, maxJumpRange):
        self.rect = pygame.Rect(32, 32, 16, 16)
        # sets how large the player's hitbox is. 
        # first two coords: top left point
        # second two coords: width & height of box
    #     self.velocity = velocity
    #     self.maxJumpRange = maxJumpRange
    # def setLocation(self, x, y):
    #     self.x = x
    #     self.y = y
    #     self.xVelocity = 0
    #     self.jumping = False
    #     self.jumpCounter = 0
    #     self.falling = True
    # def keys(self):
    #     k = pygame.key.get_pressed()
    #     if k[pygame.K_A]:
    #         self.xVelocity = -self.velocity
    #     elif k[pygame.K_D]:
    #         self.xVelocity = self.velocity
    #     else:
    #         self.xVelocity = 0
    #     if k[pygame.K_W] and not self.jumping and not self.falling:
    #         self.jumping = True
    #         self.jumpCounter = 0
    # def move(self):
    #     self.x += self.xVelocity
    #     # readd collide check here eventually lol
    #     if self.jumping:
    #         self.y -= self.velocity
    #         self.jumpCounter += 1
    #         if self.jumpCounter == self.maxJumpRange:
    #             self.jumping = False
    #             self.falling = True
    #     elif self.falling:
    #         if self.rect.colliderect(wall.rect):
    #             if xVelocity > 0:
    #                 self.rect.right = wall.rect.left
    #             if xVelocity < 0:
    #                 self.rect.left = wall.rect.left
    #             if self.jumping == True:
    #                 self.rect.bottom = wall.rect.top
    #             if self.falling = True:
    #                 self.rect.top = wall.rect.bottom
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

        