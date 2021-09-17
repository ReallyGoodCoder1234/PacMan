import pygame, sys, random

from pygame.cursors import tri_left
from Buttons import Button

from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL)

class Pac_man(pygame.sprite.Sprite):
    def __init__():
        pac_man = pygame.image.load("./Assets/Sprites/Pac_mans/Full_circ.png")
    def move_pacman(self):
        if K_LEFT == True:
            self = pygame.image.load("./Assets/Sprites/Pac_mans/Right_open.png").convert_alpha()
            self.rect.move_ip(-5, 0)
        elif K_UP == True:
            self = pygame.image.load("./Assets/Sprites/Pac_mans/pac man & life counter & death/pac man/").convert_alpha()
            self.rect.move_ip(0, -5)
        elif K_DOWN == True:
            self = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
            self.rect.move_ip(0, 5)
        elif K_RIGHT == True:
            self = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()  
            self.rect.move_ip(5, 0)
   
        def kill_pacman(surface,sounde,ghost):
            pass