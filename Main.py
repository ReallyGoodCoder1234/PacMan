from ScreenType import ScreenType
from GhostManager import GhostManager
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

ghost_manager = GhostManager()
all_ghosts =ghost_manager.ghosts

ADDGHOST = pygame.USEREVENT + 1
pygame.time.set_timer(ADDGHOST, 1200)
RELEASEGHOST = pygame.USEREVENT + 1
pygame.time.set_timer(RELEASEGHOST, 5500)


# Pac man
pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
pac_man_rect = pac_man_surface.get_rect()

# Fonts
gui_font = pygame.font.Font(None,30)

screenType = ScreenType.Main

def quite():
    pygame.quit()
    sys.exit()

def play():
    global screenType
    screenType = ScreenType.Play

def how():
    global screenType
    screenType = ScreenType.How

def credits():
    global screenType
    screenType = ScreenType.Credits

# Buttons
quit_button = Button('Quit',200,40,(25,450),6, quit)
credits_button = Button('Credits',200,40,(25,350),6, credits)
how_button = Button('How To Play',200,40,(275,450),6, how)
play_button = Button('Play',200,40,(275,350),6, play)

# Backgrounds
main_menu_background = pygame.transform.scale2x(pygame.image.load("./Assets/Levels_and_backgrounds/Main_menu_backgound.png"))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
        elif event.type == ADDGHOST and screenType == ScreenType.Play:
            ghost_manager.createGhost()

    # Draw different screen based on the current screen type
    if (screenType == ScreenType.Main):
        screen.blit(main_menu_background,(0,0))
        quit_button.draw(screen)
        credits_button.draw(screen)
        how_button.draw(screen)
        play_button.draw(screen)
    elif (screenType == ScreenType.Play):
        print("screen is play")
        sw = 1428 
        sh = 598
        screen = pygame.display.set_mode((sw,sh))
        screen.blit(pac_man_surface,(200,200))
        #Draw all ghosts
        for entity in all_ghosts:
            screen.blit(entity.surf, entity.rect)
    elif (screenType == ScreenType.How):
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
    elif (screenType == ScreenType.Credits):
        credits_text = gui_font.render('All credits go to ReallyGoodCoder1234 and MysteryCoder', True)
        credits_text_rect = credits_text.get_rect()

    pygame.display.flip()