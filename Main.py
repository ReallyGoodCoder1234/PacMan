from pygame.constants import KEYDOWN
from ScreenType import ScreenType
from GhostManager import GhostManager
import pygame, sys, random
from pygame.cursors import tri_left
from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL,K_ESCAPE)

from Buttons import Button
from Ghost import Ghost
from Pac_man import Pac_man


pygame.init()


sw = 500
sh = 500
screen = pygame.display.set_mode((sw,sh))

ghost_manager = GhostManager(598, 1598)
all_ghosts = ghost_manager.ghosts

ADDGHOST = pygame.USEREVENT + 1
pygame.time.set_timer(ADDGHOST, 1200)
RELEASEGHOST = pygame.USEREVENT + 1
pygame.time.set_timer(RELEASEGHOST, 5500)

# Pac man
pac_man = Pac_man(sw,sh,screen)

# Fonts
text_font = pygame.font.Font(None,30)
big_font = pygame.font.Font(None, 50)
bigger_font = pygame.font.Font(None, 100)

running = True
screenType = ScreenType.Main

def quit():
    pygame.quit()
    sys.exit()

def play():
    global screenType, sw, sh, screen
    screenType = ScreenType.Play
    sw = 1598
    sh = 598
    screen = pygame.display.set_mode((sw,sh))

def how():
    global screenType
    screenType = ScreenType.How

def credits():
    global screenType
    screenType = ScreenType.Credits

def escape():
    global screenType, running
    screenType = ScreenType.Main
# Buttons
quit_button = Button('Quit',200,40,(25,450),6, quit)
credits_button = Button('Credits',200,40,(25,375),6, credits)
how_button = Button('How To Play',200,40,(275,450),6, how)
play_button = Button('Play',200,40,(275,375),6, play)
escape_button = Button('Escape',200,40,(0,0),6, escape)

# Backgrounds
main_menu_background = pygame.transform.scale2x(pygame.image.load("./Assets/Levels_and_backgrounds/Main_menu_backgound.png"))

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()
        elif event.type == ADDGHOST and screenType == ScreenType.Play:
            ghost_manager.createGhost()
        if screenType == ScreenType.Play:
            pass

    screen.fill((0, 0, 0))

    # Draw different screen based on the current screen type
    if (screenType == ScreenType.Main):
        screen.blit(main_menu_background,(0,0))
        quit_button.draw(screen)
        credits_button.draw(screen)
        how_button.draw(screen)
        play_button.draw(screen)
        pygame.display.set_caption('Main Menu')
        sw = 500
        sh = 500
        screen = pygame.display.set_mode((sw,sh))
    elif (screenType == ScreenType.Play):
        #Draw all ghosts
        for entity in all_ghosts:
            screen.blit(entity.surf, entity.rect)
        escape_button.draw(screen)
        if KEYDOWN == True:
            keys = pygame.key.get_pressed
            pac_man.move_pacman(keys,598,1598)
        sw = 1598
        sh = 598
        screen = pygame.display.set_mode((sw,sh))
        all_ghosts.update()

    elif (screenType == ScreenType.How):
        screen.blit(main_menu_background,(0,0))
        how_text_level_1 = text_font.render('To play press arrow keys:', True, (0,0,0),(255,255,255))
        how_text_level_2 = text_font.render('Right key makes you move right,', True, (0,0,0),(255,255,255))
        how_text_level_3 = text_font.render('Left key makes you move Left,', True, (0,0,0),(255,255,255))
        how_text_level_4 = text_font.render('Up key makes you move up,', True, (0,0,0),(255,255,255))
        how_text_level_5 = text_font.render('Down key makes you move down.', True, (0,0,0),(255,255,255))
        how_text_level_6 = text_font.render('You cannot go through walls.', True, (0,0,0),(255,255,255))
        how_text_level_7 = text_font.render('You also cannot eat ghosts unless', True, (0,0,0),(255,255,255))
        how_text_level_8 = text_font.render('you have eaten a flashing pink dot', True, (0,0,0),(255,255,255))
        how_text_level_9 = big_font.render('HOW TO PLAY', True, (0,0,0), (0,255,0))
        how_text_level_10 = big_font.render('PAC-MAN', True, (0,0,0), (0,255,0))
        how_text_rect_9 = how_text_level_9.get_rect()
        how_text_rect_1 = how_text_level_1.get_rect()
        how_text_rect_2 = how_text_level_2.get_rect()
        how_text_rect_3 = how_text_level_3.get_rect()
        how_text_rect_4 = how_text_level_4.get_rect()
        how_text_rect_5 = how_text_level_5.get_rect()
        how_text_rect_6 = how_text_level_6.get_rect()
        how_text_rect_7 = how_text_level_7.get_rect()
        how_text_rect_8 = how_text_level_8.get_rect()
        how_text_rect_10 = how_text_level_10.get_rect()
        how_text_rect_1.center = (sw // 2, 130)
        screen.blit(how_text_level_1, how_text_rect_1)
        how_text_rect_2.center = (sw // 2, 155)
        screen.blit(how_text_level_2, how_text_rect_2)
        how_text_rect_3.center = (sw // 2, 180)
        screen.blit(how_text_level_3, how_text_rect_3)
        how_text_rect_4.center = (sw // 2, 205)
        screen.blit(how_text_level_4, how_text_rect_4)
        how_text_rect_5.center = (sw // 2, 230)
        screen.blit(how_text_level_5, how_text_rect_5)
        how_text_rect_6.center = (sw // 2, 255)
        screen.blit(how_text_level_6, how_text_rect_6)
        how_text_rect_7.center = (sw // 2, 280)
        screen.blit(how_text_level_7, how_text_rect_7)
        how_text_rect_8.center = (sw // 2, 305)
        screen.blit(how_text_level_8, how_text_rect_8)
        how_text_rect_9.center = (sw // 2, 70)
        screen.blit(how_text_level_9, how_text_rect_9)
        how_text_rect_10.center = (sw // 2, 470)
        screen.blit(how_text_level_10, how_text_rect_10)
        escape_button.draw(screen)
        pygame.display.set_caption('How To Play')
        sw = 500
        sh = 500
        screen = pygame.display.set_mode((sw,sh))
    elif (screenType == ScreenType.Credits):
        screen.blit(main_menu_background,(0,0))
        credits_text = text_font.render('All credits go to', True, (0,0,0),(255,255,255))
        credits_text_2 = text_font.render('ReallyGoodCoder1234 and MysteryCoder', True, (0,0,0),(255,255,255))
        credits_text_rect = credits_text.get_rect()
        credits_text_rect.center = (sw // 2,sh // 2)
        screen.blit(credits_text, credits_text_rect)
        credits_text_rect_2 = credits_text.get_rect()
        credits_text_rect_2.center = (140,275)
        screen.blit(credits_text_2, credits_text_rect_2)
        credits_title = bigger_font.render('Credits', True, (0,0,0), (0,255,0))
        credits_title_rect = credits_title.get_rect()
        credits_title_rect.center = (250, 80)
        screen.blit(credits_title, credits_title_rect)
        escape_button.draw(screen)
        pac_man_text = big_font.render('PAC-MAN', True, (0,0,0), (0,255,0))
        pac_man_text_rect = pac_man_text.get_rect()
        pac_man_text_rect.center = (sw // 2, 470)
        screen.blit(pac_man_text, pac_man_text_rect)
        pygame.display.set_caption('Credits')
        sw = 500
        sh = 500
        screen = pygame.display.set_mode((sw,sh))
    pygame.display.flip()

    pygame.time.Clock().tick(100)