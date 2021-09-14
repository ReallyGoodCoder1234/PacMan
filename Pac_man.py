import pygame, sys, turtle, random
from pygame import KEYDOWN
from Credits_button import credits
from Howtoplay_button import how
from Play_button import play

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, K_a, K_d, K_s, K_w

def move_pacman():
    if K_a == True:
        pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Right_open.png").convert_alpha()
        pac_man_surface.centerx -= 1
    elif K_w == True:
        pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
        pac_man_surface.centery -= 1
    elif K_s == True:
        pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
        pac_man_surface.centery += 1
    elif K_d == True:
        pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
        pac_man_surface.centerx += 1
        

pygame.init()

# Pac man
#pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
#pac_man_rect = pac_man_surface.get_rect()

sw = 1427
sh = 598
screen = pygame.display.set_mode((sw,sh))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            move_pacman()

    screen.fill((255, 255, 255))
    #screen.blit(pac_man_surface,(200,200))
    
    pygame.display.flip()