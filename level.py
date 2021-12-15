from map import Map
import pygame

class Levels:
    
    def __init__(self, screen):
        self.levelsArray = ["1", "2", "3", "4"]
        self.currentLevel = 0
        self.screen = screen
    
    def getLevelMap(self):
        map = Map(self.screen, self.levelsArray[self.currentLevel])
        return map
    
    def levelUp(self):
        self.currentLevel += 1