# Simple pygame program
# Import and initialize the pygame library
import os, sys
import pygame
from menu import *

from pygame.locals import ( # arrow keys / commmand imports
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_w,
    K_a,
    K_s,
    K_d,

)
    
    
# Define constants for the screen width and height
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Battle Tanks!")

clock = pygame.time.Clock()

menu().main_menu(screen,clock)

# Done! Time to quit.
pygame.quit()