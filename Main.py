import pygame, sys, random

from pygame.cursors import tri_left
from Buttons import Button

from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL)

def move_pacman(self):
    if K_LEFT == True:
        self = pygame.image.load("./Assets/Sprites/Pac_mans/Right_open.png").convert_alpha()
        self.rect.move_ip(-5, 0)
    elif K_UP == True:
        self = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
        self.rect.move_ip(0, -5)
    elif K_DOWN == True:
        self = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
        self.rect.move_ip(0, 5)
    elif K_RIGHT == True:
        self = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()  
        self.rect.move_ip(5, 0)
   
def kill_pacman(surface,sounde,ghost):
    pass

pygame.init()

pygame.display.set_caption('Main Menu')

sw = 500
sh = 500
screen = pygame.display.set_mode((sw,sh))

# Pac man
pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
pac_man_rect = pac_man_surface.get_rect()

# Fonts
gui_font = pygame.font.Font(None,30)

# Game Variables
game_started = False
credits_on = False
Howtoplay = False

# Buttons
quit_button = Button('Quit',200,40,(25,450),6)
credits_button = Button('Credits',200,40,(25,350),6)
how_button = Button('How To Play',200,40,(275,450),6)
play_button = Button('Play',200,40,(275,350),6)

# Backgrounds
main_menu_background = pygame.transform.scale2x(pygame.image.load("./Assets/Levels_and_backgrounds/Main_menu_backgound.png"))


# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or quit_button.pressed == True:
           print("quit") 
           pygame.quit()
           sys.exit()

        elif play_button.pressed == True:
            sw = 1428 
            sh = 598
            screen = pygame.display.set_mode((sw,sh))
            game_started = True

        elif game_started == False and credits_on == False and Howtoplay == False:
            screen.blit(main_menu_background,(0,0))
            quit_button.draw(screen)
            credits_button.draw(screen)
            how_button.draw(screen)
            play_button.draw(screen)

        elif how_button.pressed == True:
            Howtoplay == True

        elif credits_button.pressed == True:
            credits_on == True

        elif credits_on == True:
            credits_text = gui_font.render('All credits go to ReallyGoodCoder1234 and MysteryCoder', True)
            credits_text_rect = credits_text.get_rect()

        elif Howtoplay == True:
            how_text_level_1 = gui_font.render('To play press arrow keys:', True)
            how_text_level_2 = gui_font.render('Right key makes you move right,', True)
            how_text_level_3 = gui_font.render('Left key makes you move Left,', True)
            how_text_level_4 = gui_font.render('Up key makes you move up,', True)
            how_text_level_5 = gui_font.render('Down key makes you move down.', True)
            how_text_level_6 = gui_font.render('You cannot go through walls.', True)
            how_text_level_7 = gui_font.render('You also cannot eat ghosts unless', True)
            how_text_level_8 = gui_font.render('you have eaten a flashing pink dot', True)
            how_text_rect = how_text_level_1.get_rect()
            how_text_rect = how_text_level_2.get_rect()
            how_text_rect = how_text_level_3.get_rect()
            how_text_rect = how_text_level_4.get_rect()
            how_text_rect = how_text_level_5.get_rect()
            how_text_rect = how_text_level_6.get_rect()
            how_text_rect = how_text_level_7.get_rect()
            how_text_rect = how_text_level_8.get_rect()
            how_text_level_1.center = (())
        #if event.type == pygame.KEYDOWN:
        #    move_pacman(pac_man_surface)
        #elif event.type == ADDGHOST:
           # if ghost_amount < 4:
          #      ghost = Ghost()
         #       all_sprites.add(ghost)
        #    ghost_amount += 1
       # elif event.type == RELEASEGHOST:
      #      release_ghost()

    #screen.blit(pac_man_surface,(200,200))
    # Draw all ghosts
    #for entity in all_sprites:
     #   screen.blit(entity.surf, entity.rect)
    
    pygame.display.flip()