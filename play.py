import pygame
from csv import writer
from projectile import *
from level import *
from tank import *
from map import *
from constants import *
from pygame.locals import ( # arrow keys / commmand imports
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEMOTION
)



class play:
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
    
    def singleplayer(self,screen,clock, tank_type, player_name):
        # Run until the user asks to quit
        #         Game Loop
        # Must do the following things:
        # 1. Process user input
        # 2. update the state of all game obejcts
        # 3. update the display and audio output
        # 4. maintains the speed of the game
        levels = Levels(screen)
        dead = False
        while dead == False and levels.currentLevel < len(levels.levelsArray):
        
            self_coll = pygame.sprite.Group()
            if(tank_type == "Normal"):
                player = NormalTank(125,125,5,100,5)
            elif(tank_type == "Fast"):
                player = FastTank(125,125,8,100,5)
            elif(tank_type == "Sturdy"):
                player = SturdyTank(125,125,5,200,5)
            elif(tank_type == "Sniper"):
                player = SniperTank(125,125,5,100,8)
            
            self_coll.add(player)
            

            running = True
            
            # creating the sprints for tanks and projectiles
            projectile_factory = projectileFactory()
            friendly_projectiles = pygame.sprite.Group() # sprite group of projectiles
            enemy_projectiles = pygame.sprite.Group() # sprite group of projectiles
            
            # get the map for the current level
            createMap = levels.getLevelMap()

            #createMap.loadMap()
            
            while running:
                for event in pygame.event.get(): # event loop
                    if event.type == KEYDOWN: # if any key is pressed
                        if event.key == K_ESCAPE: # if escape key is pressed, we will have to have these checks for each key, might want to defer this logic to a different function
                            running = False
                            dead = True
                        elif event.type == QUIT:
                            running = False
                            dead = True
                    if event.type == MOUSEBUTTONDOWN:
                        friendly_projectiles.add(projectile_factory.createProjectile(player.x,player.y,player.currAngle,player.bulletSpeed))
                    if event.type == MOUSEMOTION:
                            player.rotate()
                    if event.type == pygame.QUIT:
                        return
        


                player.move(createMap)
                
                createMap.refreshMap(screen)

                tankBlit(player,screen)
                
                # retreiving the sprints for ai_tnaks created with the map
                ai_array = createMap.map_tanks
                for x in ai_array:
                    tankBlit(x,screen)
                    x.move(createMap)

                if pygame.time.get_ticks() % 30 == 0:
                    for x in ai_array:
                        x.rotate((player.x,player.y))
                        enemy_projectiles.add(projectile_factory.createProjectile(x.x,x.y,x.currAngle,x.bulletSpeed))
                
                
                # when projectile are shots
                if len(friendly_projectiles) != 0 or len(enemy_projectiles) != 0: # projectiles sprite group is not empty
                    for i in friendly_projectiles:
                        i.move()
                        projectileBlit(screen, i)
                    for i in enemy_projectiles:
                        i.move()
                        projectileBlit(screen, i)
                    running = createMap.projectileCollision(friendly_projectiles, enemy_projectiles, player, self_coll)
                # if ai_tnaks or player destroyed
                if not running:
                    if len(createMap.map_tanks.sprites())==0 and levels.currentLevel == 3:
                        winner = True
                        click = False
                        with open('leaderboard.csv', 'a', newline='') as write_obj:
                            csv_writer = writer(write_obj)
                            csv_writer.writerow([player_name,player.score])
                        while winner == True:
                            screen.fill((0,0,0))
                            self.draw_title('You Win', self.title_font, (255, 255, 255), screen, SCREEN_WIDTH/2, 100)
                    
                            mx, my = pygame.mouse.get_pos()
                            
                            button_3 = pygame.Rect(SCREEN_WIDTH/2 - (250/2), 600, 250, 50)

                            pygame.draw.rect(screen, (255, 0, 0), button_3)

                            self.draw_text(player_name, self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/4, 300)
                            self.draw_text(str(player.score), self.text_font, (255, 255, 255), screen, (SCREEN_WIDTH*3)/4, 300)
                            
                            
                            self.draw_text('Main Menu', self.text_font, (255, 255, 255), screen, SCREEN_WIDTH/2, 600)
                            
                            
                            if button_3.collidepoint((mx, my)):
                                if click:
                                    winner = False
                                    dead = True
                            
                    
                            click = False
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type == MOUSEBUTTONDOWN:
                                    if event.button == 1:
                                        click = True
                    
                            pygame.display.update()
                            clock.tick(60)

                    elif len(createMap.map_tanks.sprites())==0: # ai tanks defeated
                        levels.levelUp()
                    else:
                        dead = True
                        with open('leaderboard.csv', 'a', newline='') as write_obj:
                            csv_writer = writer(write_obj)
                            csv_writer.writerow(["player_name",player.score])
                
                #player.rotate()
                # the second argument is the name of the .txt file representing maps
                # these files are located in maps folder
                # TODI: change the hard coded string '2' to user choice from menu
                
                pygame.display.flip() # update the display
                clock.tick(30)
