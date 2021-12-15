import pygame
from constants import *
from tank import *
from csv import writer
from projectile import *


class Block(pygame.sprite.Sprite):
    def __init__(self,i,rect):
        super(Block, self).__init__()
        self.picture = i
        self.image = pygame.image.load(i).convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = rect

class Map:
    def __init__(self, screen, stage):
        self.map_num = '' # a string for [map].txt file in maps folder
        self.tanks = 'tanks' # array of tanks
        self.screen = screen
        self.stage = stage

        self.map_blocks = [] #string
        self.map_surfaces = pygame.sprite.Group()
        self.map_tanks = pygame.sprite.Group()
       
       # read the .txt file from stage and create the map
        with open("maps/" + self.stage + ".txt", "r") as s:
            m = [i.replace("\n", "") + (" " * (FIELDWIDTH - len(i.replace("\n", "")))) for i in s.readlines()]
            for r in range(len(m)): # loop through each string in m array representing a line from .txt file
                line = []
                for c in range(len(m[r])): # loop through each character from each line
                    line.append(m[r][c])
                    if m[r][c] == "A" or m[r][c] == "B" or m[r][c] == "C" or m[r][c] == "D" or m[r][c] == "E" or m[r][c] == "F":
                        temp_ai = aiTank(c*50,r*50,5,100,5)
                        self.map_tanks.add(temp_ai)
                    elif m[r][c] != ' ' and int(m[r][c]) >= 0:
                        block = BLOCKS[m[r][c]] # blocks will have none for white space
                        rect = pygame.Rect(c*IMAGEWIDTH, r*IMAGEHEIGHT, 50,50)
                        b = Block(block, rect)
                        self.map_surfaces.add(b)   
                self.map_blocks.append(line)


    def refreshMap(self,screen):
        screen.fill((0, 0, 0))
        for x in self.map_surfaces:
            self.screen.blit(x.image, x.rect)

                   
        
    # call this to detect collision between a tank and a block
    def detectCollision(self,objRect):
        for i in self.map_surfaces: # array should loop through each block
          if( pygame.Rect.colliderect(i.rect, objRect) == True):
                return True
        return False

        
    # projectile collision with anythin on the map
    def projectileCollision(self,friendly_projectiles, enemy_projectiles, player, self_coll, player_name):
           
        collisions = pygame.sprite.groupcollide(friendly_projectiles, self.map_surfaces, True, False) #collision with friendly proj and map
        self.projectileBlockCollision(collisions)
        collisions = pygame.sprite.groupcollide(enemy_projectiles, self.map_surfaces, True, False) #collision with enemy proj and map
        self.projectileBlockCollision(collisions)

        collisions = pygame.sprite.groupcollide(friendly_projectiles, self.map_tanks, True, False)
        for x in collisions:
            self.map_tanks.remove(collisions[x][0])
            player.score += 50
            if len(self.map_tanks.sprites())==0:
                return False

        collisions = pygame.sprite.groupcollide(enemy_projectiles, self_coll, True, False) #collisions with enmy proj and player
        if collisions:
            if(player.health == 200):
                player.health -= 100
                return True
            return False
        return True
  
  
    
    def projectileBlockCollision(self, collisions):
        for x in collisions:
            # for blue block destroy when collision
            if collisions[x][0].picture == BLOCKS["2"]:
                self.map_surfaces.remove(collisions[x][0])
            # for green block change it to blue when collision
            elif collisions[x][0].picture == BLOCKS["3"]:
                collisions[x][0].picture = BLOCKS["2"]


