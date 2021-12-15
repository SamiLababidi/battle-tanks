
import pygame
import math
import random
from constants import *

from abc import ABCMeta, abstractmethod  #https://stackoverflow.com/questions/13646245/is-it-possible-to-make-abstract-classes-in-python
class Tank: #abstract class
    __metaclass__ = ABCMeta
    @abstractmethod
    def rotate(self,target):
        pass
    @abstractmethod
    def move(self,map):
        pass
   
class aiTank(pygame.sprite.Sprite):
    def __init__(self,xInit, yInit, speed, health, bulletSpeed): # constructor , also defines the class variables
        super(aiTank,self).__init__()
        self.speed = speed
        self.health = health
        self.score = 50
        self.x = xInit
        self.y = yInit
        self.currAngle = 0
        self.bulletSpeed = bulletSpeed
        self.image1 = pygame.Surface((70,50), pygame.SRCALPHA) # base tank rectangles
        self.image2 = pygame.image.load('assets/images/innertank_blue.png')
        self.image2 = pygame.transform.scale(self.image2, (70,50))
        self.image2rot = self.image2.copy()
        self.image1.fill((22,141,196))
        self.rect = self.image1.get_rect(center=(self.x + 35, self.y + 25))

    def move(self,map):
        rect = self.image2rot.get_rect(center = (self.x+35, self.y+20))
        choice  = random.choice(["up","down","left","right"])
        if choice == "down": # down key
            y = self.y + self.speed
            rect = self.image2rot.get_rect(center = (self.x+35, y+20))
            if not map.detectCollision(rect):
                self.y += self.speed # move down
        elif choice == "up": # up key
            y = self.y - self.speed
            rect = self.image2rot.get_rect(center = (self.x+35, y+20))
            if not map.detectCollision(rect):
                self.y -= self.speed # move up
        elif choice == "right": # right key
            x = self.x + self.speed
            rect = self.image2rot.get_rect(center = (x+35, self.y+20))
            if not map.detectCollision(rect):
                self.x += self.speed # move right
        elif choice == "left": # left key
            x = self.x - self.speed
            rect = self.image2rot.get_rect(center = (x+35, self.y+20))
            if not map.detectCollision(rect):
                self.x -= self.speed # move left
        rect = self.image2rot.get_rect(center = (self.x+35, self.y+20))
        self.rect = rect

    def rotate(self, target=""):
        #calculate rotation angle
        mouse_x,mouse_y = pygame.mouse.get_pos()
        if target != "":
            mouse_x,mouse_y = target
        center_x, center_y = (self.x + 35, self.y + 25)
        rel_x, rel_y = mouse_x - center_x, mouse_y - center_y
        angle = math.atan2(rel_y, rel_x)
        angle = angle - math.pi
        angle = int((180 / math.pi) * angle * -1) - 180 
        self.currAngle = angle

        #set rotation image
        rot_image2 = pygame.transform.rotozoom(self.image2, angle,1)
        rotated_rect = rot_image2.get_rect(center = (self.x+42, self.y+25))
        self.rect = rotated_rect
        self.image2rot = rot_image2
    
class FastTank(pygame.sprite.Sprite):
    def __init__(self,xInit, yInit, speed, health, bulletSpeed): # constructor , also defines the class variables
        super(FastTank,self).__init__()
        self.speed = speed
        self.health = health
        self.score = 50
        self.x = xInit
        self.y = yInit
        self.currAngle = 0
        self.bulletSpeed = bulletSpeed
        self.image1 = pygame.Surface((70,50), pygame.SRCALPHA) # base tank rectangles
        self.image2 = pygame.image.load('assets/images/innertank.png')
        self.image2 = pygame.transform.scale(self.image2, (70,50))
        self.image2rot = self.image2.copy()
        self.image1.fill((255,0,0))
        self.rect = self.image1.get_rect(center=(self.x + 35, self.y + 25))

    
    def rotate(self, target=""):
        #calculate rotation angle
        mouse_x,mouse_y = pygame.mouse.get_pos()
        if target != "":
            mouse_x,mouse_y = target
        center_x, center_y = (self.x + 35, self.y + 25)
        rel_x, rel_y = mouse_x - center_x, mouse_y - center_y
        angle = math.atan2(rel_y, rel_x)
        angle = angle - math.pi
        angle = int((180 / math.pi) * angle * -1) - 180 
        self.currAngle = angle


        #set rotation image
        rot_image2 = pygame.transform.rotozoom(self.image2, angle,1)
        rotated_rect = rot_image2.get_rect(center = (self.x+42, self.y+25))
        self.rect = rotated_rect
        self.image2rot = rot_image2

    def move(self,map):
        rect = self.image2rot.get_rect(center = (self.x+35, self.y+20))
        key = pygame.key.get_pressed() # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN] or key[pygame.K_s]: # down key
            y = self.y + self.speed
            rect = self.image2rot.get_rect(center = (self.x+35, y+20))
            if not map.detectCollision(rect):
                self.y += self.speed # move down
        elif key[pygame.K_UP] or key[pygame.K_w]: # up key
            y = self.y - self.speed
            rect = self.image2rot.get_rect(center = (self.x+35, y+20))
            if not map.detectCollision(rect):
                self.y -= self.speed # move up
        elif key[pygame.K_RIGHT] or key[pygame.K_d]: # right key
            x = self.x + self.speed
            rect = self.image2rot.get_rect(center = (x+35, self.y+20))
            if not map.detectCollision(rect):
                self.x += self.speed # move right
        elif key[pygame.K_LEFT] or key[pygame.K_a]: # left key
            x = self.x - self.speed
            rect = self.image2rot.get_rect(center = (x+35, self.y+20))
            if not map.detectCollision(rect):
                self.x -= self.speed # move left
        rect = self.image2rot.get_rect(center = (self.x+35, self.y+20))
        self.rect = rect

        # Keep player on the screen

    
       


        

class SturdyTank(pygame.sprite.Sprite):
    def __init__(self,xInit, yInit, speed, health, bulletSpeed): # constructor , also defines the class variables
        super(SturdyTank,self).__init__()
        self.speed = speed
        self.health = health
        self.score = 50
        self.x = xInit
        self.y = yInit
        self.currAngle = 0
        self.bulletSpeed = bulletSpeed
        self.image1 = pygame.Surface((70,50), pygame.SRCALPHA) # base tank rectangles
        self.image2 = pygame.image.load('assets/images/innertank_green.png')
        self.image2 = pygame.transform.scale(self.image2, (70,50))
        self.image2rot = self.image2.copy()
        self.image1.fill((101,184,142))
        self.rect = self.image1.get_rect(center=(self.x + 35, self.y + 25))

    
    def rotate(self, target=""):
        #calculate rotation angle
        mouse_x,mouse_y = pygame.mouse.get_pos()
        if target != "":
            mouse_x,mouse_y = target
        center_x, center_y = (self.x + 35, self.y + 25)
        rel_x, rel_y = mouse_x - center_x, mouse_y - center_y
        angle = math.atan2(rel_y, rel_x)
        angle = angle - math.pi
        angle = int((180 / math.pi) * angle * -1) - 180 
        self.currAngle = angle


        #set rotation image
        rot_image2 = pygame.transform.rotozoom(self.image2, angle,1)
        rotated_rect = rot_image2.get_rect(center = (self.x+42, self.y+25))
        self.rect = rotated_rect
        self.image2rot = rot_image2

    def move(self,map):
        rect = self.image2rot.get_rect(center = (self.x+35, self.y+20))
        key = pygame.key.get_pressed() # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN] or key[pygame.K_s]: # down key
            y = self.y + self.speed
            rect = self.image2rot.get_rect(center = (self.x+35, y+20))
            if not map.detectCollision(rect):
                self.y += self.speed # move down
        elif key[pygame.K_UP] or key[pygame.K_w]: # up key
            y = self.y - self.speed
            rect = self.image2rot.get_rect(center = (self.x+35, y+20))
            if not map.detectCollision(rect):
                self.y -= self.speed # move up
        elif key[pygame.K_RIGHT] or key[pygame.K_d]: # right key
            x = self.x + self.speed
            rect = self.image2rot.get_rect(center = (x+35, self.y+20))
            if not map.detectCollision(rect):
                self.x += self.speed # move right
        elif key[pygame.K_LEFT] or key[pygame.K_a]: # left key
            x = self.x - self.speed
            rect = self.image2rot.get_rect(center = (x+35, self.y+20))
            if not map.detectCollision(rect):
                self.x -= self.speed # move left
        rect = self.image2rot.get_rect(center = (self.x+35, self.y+20))
        self.rect = rect

class SniperTank(pygame.sprite.Sprite):
    def __init__(self,xInit, yInit, speed, health, bulletSpeed): # constructor , also defines the class variables
        super(SniperTank,self).__init__()
        self.speed = speed
        self.health = health
        self.score = 50
        self.x = xInit
        self.y = yInit
        self.currAngle = 0
        self.bulletSpeed = bulletSpeed
        self.image1 = pygame.Surface((70,50), pygame.SRCALPHA) # base tank rectangles
        self.image2 = pygame.image.load('assets/images/innertank_yellow.png')
        self.image2 = pygame.transform.scale(self.image2, (70,50))
        self.image2rot = self.image2.copy()
        self.image1.fill((233,255,125))
        self.rect = self.image1.get_rect(center=(self.x + 35, self.y + 25))

    
    def rotate(self, target=""):
        #calculate rotation angle
        mouse_x,mouse_y = pygame.mouse.get_pos()
        if target != "":
            mouse_x,mouse_y = target
        center_x, center_y = (self.x + 35, self.y + 25)
        rel_x, rel_y = mouse_x - center_x, mouse_y - center_y
        angle = math.atan2(rel_y, rel_x)
        angle = angle - math.pi
        angle = int((180 / math.pi) * angle * -1) - 180 
        self.currAngle = angle


        #set rotation image
        rot_image2 = pygame.transform.rotozoom(self.image2, angle,1)
        rotated_rect = rot_image2.get_rect(center = (self.x+42, self.y+25))
        self.rect = rotated_rect
        self.image2rot = rot_image2

    def move(self,map):
        rect = self.image2rot.get_rect(center = (self.x+35, self.y+20))
        key = pygame.key.get_pressed() # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN] or key[pygame.K_s]: # down key
            y = self.y + self.speed
            rect = self.image2rot.get_rect(center = (self.x+35, y+20))
            if not map.detectCollision(rect):
                self.y += self.speed # move down
        elif key[pygame.K_UP] or key[pygame.K_w]: # up key
            y = self.y - self.speed
            rect = self.image2rot.get_rect(center = (self.x+35, y+20))
            if not map.detectCollision(rect):
                self.y -= self.speed # move up
        elif key[pygame.K_RIGHT] or key[pygame.K_d]: # right key
            x = self.x + self.speed
            rect = self.image2rot.get_rect(center = (x+35, self.y+20))
            if not map.detectCollision(rect):
                self.x += self.speed # move right
        elif key[pygame.K_LEFT] or key[pygame.K_a]: # left key
            x = self.x - self.speed
            rect = self.image2rot.get_rect(center = (x+35, self.y+20))
            if not map.detectCollision(rect):
                self.x -= self.speed # move left
        rect = self.image2rot.get_rect(center = (self.x+35, self.y+20))
        self.rect = rect


class NormalTank(pygame.sprite.Sprite):
    def __init__(self,xInit, yInit, speed, health, bulletSpeed): # constructor , also defines the class variables
        super(NormalTank,self).__init__()
        self.speed = speed
        self.health = health
        self.score = 50
        self.x = xInit
        self.y = yInit
        self.currAngle = 0
        self.bulletSpeed = bulletSpeed
        self.image1 = pygame.Surface((70,50), pygame.SRCALPHA) # base tank rectangles
        self.image2 = pygame.image.load('assets/images/innertank_grey.png')
        self.image2 = pygame.transform.scale(self.image2, (70,50))
        self.image2rot = self.image2.copy()
        self.image1.fill((222,222,222))
        self.rect = self.image1.get_rect(center=(self.x + 35, self.y + 25))

    
    def rotate(self, target=""):
        #calculate rotation angle
        mouse_x,mouse_y = pygame.mouse.get_pos()
        if target != "":
            mouse_x,mouse_y = target
        center_x, center_y = (self.x + 35, self.y + 25)
        rel_x, rel_y = mouse_x - center_x, mouse_y - center_y
        angle = math.atan2(rel_y, rel_x)
        angle = angle - math.pi
        angle = int((180 / math.pi) * angle * -1) - 180 
        self.currAngle = angle


        #set rotation image
        rot_image2 = pygame.transform.rotozoom(self.image2, angle,1)
        rotated_rect = rot_image2.get_rect(center = (self.x+42, self.y+25))
        self.rect = rotated_rect
        self.image2rot = rot_image2

    def move(self,map):
        rect = self.image2rot.get_rect(center = (self.x+35, self.y+20))
        key = pygame.key.get_pressed() # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN] or key[pygame.K_s]: # down key
            y = self.y + self.speed
            rect = self.image2rot.get_rect(center = (self.x+35, y+20))
            if not map.detectCollision(rect):
                self.y += self.speed # move down
        elif key[pygame.K_UP] or key[pygame.K_w]: # up key
            y = self.y - self.speed
            rect = self.image2rot.get_rect(center = (self.x+35, y+20))
            if not map.detectCollision(rect):
                self.y -= self.speed # move up
        elif key[pygame.K_RIGHT] or key[pygame.K_d]: # right key
            x = self.x + self.speed
            rect = self.image2rot.get_rect(center = (x+35, self.y+20))
            if not map.detectCollision(rect):
                self.x += self.speed # move right
        elif key[pygame.K_LEFT] or key[pygame.K_a]: # left key
            x = self.x - self.speed
            rect = self.image2rot.get_rect(center = (x+35, self.y+20))
            if not map.detectCollision(rect):
                self.x -= self.speed # move left
        rect = self.image2rot.get_rect(center = (self.x+35, self.y+20))
        self.rect = rect



class TankFactory:
    def getTank(self, tankType):
        pass


def tankBlit(tank,screen):
    
    screen.blit(tank.image1, tank.image1.get_rect(center = (tank.x+42, tank.y+25)))
    screen.blit(tank.image2rot, tank.rect)
    
    #screen.blit(tank.image3rot, (tank.x + 42, tank.y + 22))


