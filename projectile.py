import pygame
import math


def projectileBlit(screen, projectile):
    screen.blit(projectile.rotImage, projectile.pos)

class projectileFactory():
    def __init__(self):
        return
    def createProjectile(self,x,y,angle, speed): #factory pattern
        xdir = math.cos(math.radians(angle))
        ydir = -1 * math.sin(math.radians(angle))
        direction = (xdir, ydir)
        xinit = (x + 35) + 20 * xdir
        yinit = (y + 18) + 15 * ydir
        proj = projectile(xinit, yinit, speed, direction)
        proj.setRotation(angle)
        return proj

def deleteProjectiles(projectiles,map):
    for x in projectiles:
        rect = (x.pos.x,x.pos.y,10,10)
        if(map.detectCollision(rect) == True):
            projectiles.remove(x)


class projectile(pygame.sprite.Sprite):
    def __init__(self,x,y,speed, startDir):
        super(projectile,self).__init__()
        self.pos = (x,y)
        self.numWallTouches = 0
        self.speed = speed

        self.image = pygame.image.load('assets/images/bullet.png')
        self.image = pygame.transform.scale(self.image, (10,10))
        self.rect = self.image.get_rect()
        self.rotImage = self.image.copy()

        self.dir = pygame.math.Vector2(startDir).normalize() #set direction

    def setRotation(self, angle):
        rot_image = self.image.copy()
        rot_image = pygame.transform.rotozoom(self.image, angle,1)
        self.rotImage = rot_image

    
    def move(self):
        self.pos += self.speed * self.dir
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 10,10)
        # self.rect.center = round(self.pos.x), round(self.pos.y)

        



    




