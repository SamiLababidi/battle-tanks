import pygame
import csv
import pandas as pd
from play import *
from pygame.locals import ( # arrow keys / commmand imports
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_BACKSPACE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
)
    
# class button:
#     def __init__(self,x,y,w,h,screen,function):
#         pos = pygame.mouse.get_pos()
#         click = pygame.mouse.get_pressed()

#         if pos[0] > x and pos[0] < x + w and pos[1] > y and pos[1] < y + h:
#             if click[0] == 1:
#                 function.clicked(screen) #change event with botton here
#         pygame.draw.rect(screen, (255,255,255), (x,y,w,h))

class menu:
    def __init__(self):
        self.title_font = pygame.font.Font("assets/fonts/airstrip.ttf", 80)
        self.text_font = pygame.font.Font("assets/fonts/NEON GLOW-Light.otf", 40)

    def draw_title(self,text, font, color, surface, x, y): 
        textobj = font.render(text, 1, color)
        text_width = textobj.get_width()
        textrect = textobj.get_rect()
        textrect.topleft = (x-(text_width/2), y)
        surface.blit(textobj, textrect)
    
    def draw_text(self,text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        text_width = textobj.get_width()
        textrect = textobj.get_rect()
        textrect.topleft = (x-(text_width/2), y)
        surface.blit(textobj, textrect)

    def main_menu(self,screen,clock):
        while True:
            screen.fill((0,0,0))
            self.draw_title('Battle Tanks', self.title_font, (255, 255, 255), screen, SCREEN_WIDTH/2, 100)
    
            mx, my = pygame.mouse.get_pos()
    
            
            button_1 = pygame.Rect(SCREEN_WIDTH/2 - 105, 300, 210, 50)
            button_3 = pygame.Rect(SCREEN_WIDTH/2 - (250/2), 600, 250, 50)

            pygame.draw.rect(screen, (255, 0, 0), button_1)
            pygame.draw.rect(screen, (255, 0, 0), button_3)

            self.draw_text('Singleplayer', self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/2, 300)
            self.draw_text('Leaderboards', self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/2, 600)
            


            if button_1.collidepoint((mx, my)):
                if click:
                    self.preGame(screen,clock)
            if button_3.collidepoint((mx, my)):
                if click:
                    self.leaderboards(screen,clock)
            
            
    
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            clock.tick(60)
    
    # display the leaderboard
    def leaderboards(self,screen,clock):
        working = True
        while working:
            screen.fill((0,0,0))
            self.draw_title('Top 5 Scores', self.title_font, (255, 255, 255), screen, SCREEN_WIDTH/2, 100)
    
            mx, my = pygame.mouse.get_pos()
    
            
            button_1 = pygame.Rect(SCREEN_WIDTH/2 - 105, 200, 210, 50)
            pygame.draw.rect(screen, (255, 0, 0), button_1)
            self.draw_text('Main Menu', self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/2, 200)
            

            Scores = pd.read_csv("leaderboard.csv")
            Scores = Scores.sort_values("Score", ascending=False).reset_index(drop=True)

            self.draw_text(Scores['Name'][0], self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/4, 300)
            self.draw_text(str(Scores['Score'][0]), self.text_font, (255, 255, 255), screen, (SCREEN_WIDTH*3)/4, 300)

            self.draw_text(Scores['Name'][1], self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/4, 400)
            self.draw_text(str(Scores['Score'][1]), self.text_font, (255, 255, 255), screen, (SCREEN_WIDTH*3)/4, 400)

            self.draw_text(Scores['Name'][2], self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/4, 500)
            self.draw_text(str(Scores['Score'][2]), self.text_font, (255, 255, 255), screen, (SCREEN_WIDTH*3)/4, 500)

            self.draw_text(Scores['Name'][3], self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/4, 600)
            self.draw_text(str(Scores['Score'][3]), self.text_font, (255, 255, 255), screen, (SCREEN_WIDTH*3)/4, 600)

            self.draw_text(Scores['Name'][4], self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/4, 700)
            self.draw_text(str(Scores['Score'][4]), self.text_font, (255, 255, 255), screen, (SCREEN_WIDTH*3)/4, 700)



            if button_1.collidepoint((mx, my)):
                if click:
                    working = False
            
            
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            clock.tick(60)

    def preGame(self,screen,clock):
        working = True
        text_input = ''
        while working:
            screen.fill((0,0,0))
            self.draw_title('Choose Name and Tank', self.title_font, (255, 255, 255), screen, SCREEN_WIDTH/2, 100)
    
            mx, my = pygame.mouse.get_pos()
    
            
            button_1 = pygame.Rect(SCREEN_WIDTH/2 - 105, 200, 210, 50)
            pygame.draw.rect(screen, (255, 0, 0), button_1)
            self.draw_text('Main Menu', self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/2, 200)
            
            
            
            text_field = pygame.Rect(SCREEN_WIDTH/2 - 105, 350, 210, 50)
            pygame.draw.rect(screen, (255, 255, 255), text_field)
            self.draw_text('Name', self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/2, 300)
            self.draw_text(text_input, self.text_font, (0,0,0), screen, SCREEN_WIDTH/2, 350)



            button_2 = pygame.Rect(SCREEN_WIDTH/4 - 250, 500, 220, 50)
            pygame.draw.rect(screen, (0, 0, 255), button_2)
            self.draw_text('Normal Tank', self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/4-140, 500)

            button_3 = pygame.Rect(SCREEN_WIDTH/2 - 250, 500, 220, 50)
            pygame.draw.rect(screen, (255, 0, 0), button_3)
            self.draw_text('Fast Tank', self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/2-140, 500)

            button_4 = pygame.Rect((3*SCREEN_WIDTH)/4 - 250, 500, 220, 50)
            pygame.draw.rect(screen, (255, 0, 0), button_4)
            self.draw_text('Sniper Tank', self.text_font, (255, 255, 255), screen, (3*SCREEN_WIDTH)/4-140, 500)
            
            button_5 = pygame.Rect(SCREEN_WIDTH - 250, 500, 220, 50)
            pygame.draw.rect(screen, (255, 0, 0), button_5)
            self.draw_text('Sturdy Tank', self.text_font, (255, 255, 255), screen, SCREEN_WIDTH-140, 500)
            



            if button_1.collidepoint((mx, my)):
                if click:
                    working = False

            if button_2.collidepoint((mx, my)) and text_input != '':
                if click:
                    play().singleplayer(screen,clock,"Normal",text_input)
            if button_3.collidepoint((mx, my)) and text_input != '':
                if click:
                    play().singleplayer(screen,clock,"Fast",text_input)
            if button_4.collidepoint((mx, my)) and text_input != '':
                if click:
                    play().singleplayer(screen,clock,"Sniper",text_input)
            if button_5.collidepoint((mx, my)) and text_input != '':
                if click:
                    play().singleplayer(screen,clock,"Sturdy",text_input)
            
            
            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == K_BACKSPACE:
                        if text_input != '':
                            text_input = text_input[:-1]
                    else:
                        text_input = text_input + event.unicode

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            clock.tick(60)

