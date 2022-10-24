import pygame, sys, random
from pygame.cursors import tri_left
from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL,K_ESCAPE,KEYDOWN)
from pygame import mixer
import GLOBABAL

from Buttons import Button
from Ghost import Ghost
from Pac_man import Pac_man
from ScreenType import ScreenType
from GhostManager import GhostManager
from Map import MapCreator



mixer.init()
mixer.music.load("./Assets/Music/pacman_eatfruit.wav")
mixer.music.set_volume(100)

#screen
pygame.init()
sw = 560
sh = 620
screen = pygame.display.set_mode((sw,sh))
collided = False

#Wall
MapC = MapCreator()
MapC.download_level("Wall map.txt", "Pellet map.txt", "Power map.txt")
MapC.create_pellet()
MapC.create_walls()
MapC.create_power()

#Ghost
ghost_manager = GhostManager(598, 1598)
all_ghosts = ghost_manager.ghosts

ADDGHOST = pygame.USEREVENT + 1
pygame.time.set_timer(ADDGHOST, 1200)
FLASHGOHST = pygame.USEREVENT + 2
pygame.time.set_timer(FLASHGOHST, 200)
RELEASEGHOST = pygame.USEREVENT + 3
pygame.time.set_timer(RELEASEGHOST, 5500)
KILLBOY = pygame.USEREVENT + 4

# Pac man
pac_man = Pac_man(sh,sw,screen, MapC)

# Fonts
text_font = pygame.font.Font(None,30)
big_font = pygame.font.Font(None, 50)
bigger_font = pygame.font.Font(None, 100)
giant_font = pygame.font.Font(None, 200)

#Screens
running = True
screenType = ScreenType.Main

def quit():
    pygame.quit()
    sys.exit()

def play():
    global screenType, sw, sh, screen
    screenType = ScreenType.Play

def how():
    global screenType
    screenType = ScreenType.How

def credits():
    global screenType
    screenType = ScreenType.Credits

def escape():
    global screenType, running
    screenType = ScreenType.Main

def draw_background(pic,sw,sh):
    background = pygame.image.load(pic).convert_alpha()
    background_rect = background.get_rect()
    background = pygame.transform.scale(background,(sw,sh))
    screen.blit(background,(0,0))

# Buttons
quit_button = Button('Exit',200,40,(50,530),6, quit)
credits_button = Button('Credits',200,40,(50,455),6, credits)
how_button = Button('How To Play',200,40,(300,530),6, how)
play_button = Button('Play',200,40,(300,455),6, play)
escape_button = Button('Back',200,40,(0,0),6, escape)

# Backgrounds
main_menu_background = pygame.transform.scale2x(pygame.image.load("./Assets/Levels_and_backgrounds/Main_menu_backgound.png"))
# Game loop
while running:
    for event in pygame.event.get():
        #Quit
        if event.type == pygame.QUIT or GLOBABAL.game == True:
           pygame.quit()
           sys.exit()
        #Create Ghost
        elif event.type == ADDGHOST and screenType == ScreenType.Play:
            ghost_manager.createGhost(MapC)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and pac_man.collides.get("left") == False:
                pac_man.direction = "left"
            if event.key == pygame.K_d and pac_man.collides.get("right") == False:
                pac_man.direction = "right"
            if event.key == pygame.K_w and pac_man.collides.get("up") == False:
                pac_man.direction = "up"
            if event.key == pygame.K_s and pac_man.collides.get("down") == False:
                pac_man.direction = "down"
        #Flash Ghost
        elif event.type == FLASHGOHST and screenType == ScreenType.Play:
            if GLOBABAL.cankill == True:
                pass
            for entity in all_ghosts:
                entity.flashImage()

    screen.fill((0, 0, 0))

    #Screen Text
    if (screenType == ScreenType.Main):
        screen.blit(main_menu_background,(0,0))
        quit_button.draw(screen)
        credits_button.draw(screen)
        how_button.draw(screen)
        play_button.draw(screen)
        text = giant_font.render('Pac Man', True, (255,255,255), (203,197,198))
        text_rect = text.get_rect()
        text_rect.center = (sw // 2, 200)
        screen.blit(text, text_rect)
        text2 = big_font.render("(But it's robot invasion)", True, (255,255,255), (203,197,198))
        text2_rect = text.get_rect()
        text2_rect.center = (400, 400)
        screen.blit(text2, text2_rect)
        text3 = big_font.render("Scope It Edition", True, (255,255,255), (0,0,0))
        text3_rect = text.get_rect()
        text3_rect.center = (370, 150)
        screen.blit(text3, text3_rect)
        pygame.display.set_caption('Main Menu')

    elif (screenType == ScreenType.How):
        screen.blit(main_menu_background,(0,0))
        how_text_level_1 = text_font.render('To play press the following keys:', True, (0,0,0),(255,255,255))
        how_text_level_2 = text_font.render('The a key makes you move right,', True, (0,0,0),(255,255,255))
        how_text_level_3 = text_font.render('The d key makes you move Left,', True, (0,0,0),(255,255,255))
        how_text_level_4 = text_font.render('The w key makes you move up,', True, (0,0,0),(255,255,255))
        how_text_level_5 = text_font.render('The s key makes you move down.', True, (0,0,0),(255,255,255))
        how_text_level_6 = text_font.render('You cannot go through walls.', True, (0,0,0),(255,255,255))
        how_text_level_7 = text_font.render('You also cannot eat ghosts unless', True, (0,0,0),(255,255,255))
        how_text_level_8 = text_font.render('you have eaten a big yellow dot', True, (0,0,0),(255,255,255))
        how_text_level_9 = big_font.render('HOW TO PLAY', True, (255,255,255), (203,197,198))
        how_text_level_10 = big_font.render('PAC-MAN', True, (255,255,255), (203,197,198))
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

    elif (screenType == ScreenType.Credits):
        screen.blit(main_menu_background,(0,0))
        credits_text = text_font.render('All credits go to:', True, (0,128,128),(0,0,0))
        credits_text_2 = text_font.render('ReallyGoodCoder1234', True, (135,206,235),(0,0,0))
        credits_text_3 = text_font.render('but not really MysteryCoder', True, (30,144,255),(0,0,0))
        credits_text_rect = credits_text.get_rect()
        credits_text_rect.center = (sw // 2, 275)
        screen.blit(credits_text, credits_text_rect)
        credits_text_rect_2 = credits_text.get_rect()
        credits_text_rect_2.center = (sw//2,sh//2)
        screen.blit(credits_text_2, credits_text_rect_2)
        credits_text_rect_3 = credits_text.get_rect()
        credits_text_rect_3.center = (sw//2,sh//2+30)
        screen.blit(credits_text_3, credits_text_rect_3)
        credits_title = bigger_font.render('Credits', True, (255,255,255), (203,197,198))
        credits_title_rect = credits_title.get_rect()
        credits_title_rect.center = (sw//2, 80)
        screen.blit(credits_title, credits_title_rect)
        escape_button.draw(screen)
        pac_man_text = big_font.render('PAC-MAN', True, (255,255,255), (203,197,198))
        pac_man_text_rect = pac_man_text.get_rect()
        pac_man_text_rect.center = (sw // 2, 470)
        screen.blit(pac_man_text, pac_man_text_rect)
        pygame.display.set_caption('Credits')

    elif (screenType == ScreenType.Play):

        for spr in pac_man.map.walls:
            screen.blit(spr.surf, spr.rect)
        pac_man.map.walls.update()
        if GLOBABAL.lives > 0:
            draw_background("./Assets/Levels_and_backgrounds/Pac_man_maze.png",sw,sh)
        for spr in pac_man.map.pellets:
            screen.blit(spr.surf, spr.rect)
        pac_man.map.pellets.update()
        for spr in pac_man.map.powers:
            screen.blit(spr.surf, spr.rect)
        pac_man.map.powers.update()
        #Draw all ghosts
        for entity in all_ghosts:
            screen.blit(entity.surf, entity.rect)
        all_ghosts.update()
        if pac_man.killed == False:
            pac_man.move_pacman()
            pac_man.kill_pacman(all_ghosts, screen, ghost_manager)
            screen.blit(pac_man.surf,pac_man.rect)
        if GLOBABAL.lives > 0:
            score_text = text_font.render(str(GLOBABAL.score), True, (0,0,0), (0,255,0))
            score_text_rect = score_text.get_rect()
            score_text_rect.center = (280, 10)
            screen.blit(score_text, score_text_rect)
        if GLOBABAL.cankill == True:
            seconds = (pygame.time.get_ticks()-pac_man.tick)/1000
            if seconds >= 10:
                GLOBABAL.cankill = False
                for x in all_ghosts:
                    x.hasImage = True
        

        if GLOBABAL.lives == 0:
            game_text = text_font.render("GAME OVER", True, (0,0,0), (0,255,0))
            game_text_rect = game_text.get_rect()
            game_text_rect.center = (280, 310)
            screen.blit(game_text, game_text_rect)
            MapC.pellets.empty()
            MapC.walls.empty()
            MapC.powers.empty()
            all_ghosts.empty()
            quit_button.draw(screen)
        if pac_man.killed == True:
            pac_man = Pac_man(sh,sw,screen, MapC)
        if GLOBABAL.lives == 3:
            one = pygame.image.load("./Assets/Sprites/Pac_mans/Right_open.png")
            one_rect = one.get_rect()
            one_rect.center = (10, 610)
            screen.blit(one, one_rect)
            two = pygame.image.load("./Assets/Sprites/Pac_mans/Right_open.png")
            two_rect = two.get_rect()
            two_rect.center = (30, 610)
            screen.blit(two, two_rect)
            three = pygame.image.load("./Assets/Sprites/Pac_mans/Right_open.png")
            three_rect = three.get_rect()
            three_rect.center = (50, 610)
            screen.blit(three, three_rect)
        if GLOBABAL.lives == 2:
            one = pygame.image.load("./Assets/Sprites/Pac_mans/Right_open.png")
            one_rect = one.get_rect()
            one_rect.center = (10, 610)
            screen.blit(one, one_rect)
            two = pygame.image.load("./Assets/Sprites/Pac_mans/Right_open.png")
            two_rect = two.get_rect()
            two_rect.center = (30, 610)
            screen.blit(two, two_rect)
        if GLOBABAL.lives == 1:
            one = pygame.image.load("./Assets/Sprites/Pac_mans/Right_open.png")
            one_rect = one.get_rect()
            one_rect.center = (10, 610)
            screen.blit(one, one_rect)
            


    #Update
    pygame.display.flip()
    pygame.time.Clock().tick(240)