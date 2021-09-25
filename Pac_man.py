import pygame, sys, random

from pygame.cursors import tri_left
from Buttons import Button

from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL)

class Pac_man(pygame.sprite.Sprite):
    def __init__():
        global pac_man_rect
        pac_man = pygame.image.load("./Assets/Sprites/Pac_mans/Full_circ.png")
        pac_man_rect = pygame.get_rect(pac_man)
    def move_pacman(self,keys):
        
        vel = 10
        if keys[pygame.K_LEFT] and pac_man_rect.centerx>0:
            pac_man_rect.centerx -= vel
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