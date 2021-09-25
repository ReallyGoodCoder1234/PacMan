from ScreenType import ScreenType
import pygame, sys, random

from pygame.cursors import tri_left
from Buttons import Button

from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL,K_ESCAPE)

class Pac_man(pygame.sprite.Sprite):
    def __init__(self, maxHeight, maxWidth,screen):
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth
        super(Pac_man, self).__init__()
        image = "./Assets/Sprites/Pac_mans/Full_circ.png"
        self.surf = pygame.image.load(image).convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.speed = 1
        screen.blit(self.surf,self.rect)

    def move_pacman(self, keys, sw, sh):
        vel = 1

        if keys[K_w] == True and pac_man_rect.top == 0:
            self.rect.centery -= vel
            image = "./Assets/Sprites/Pac_mans/"
            self.surf = pygame.image.load(image).convert_alpha()
        elif keys[K_s] == True and pac_man_rect.top == self.maxHeight:
            self.rect.centery += vel
            image = "./Assets/Sprites/Pac_mans/Full_circ.png"
            self.surf = pygame.image.load(image).convert_alpha()
        elif keys[K_a] == True and pac_man_rect.top == 0:
            self.rect.centerx -= vel
            image = "./Assets/Sprites/Pac_mans/Full_circ.png"
            self.surf = pygame.image.load(image).convert_alpha()
        elif keys[K_d] == True and pac_man_rect.top == self.maxWidth:
            self.rect.centerx += vel
            image = "./Assets/Sprites/Pac_mans/Full_circ.png"
            self.surf = pygame.image.load(image).convert_alpha()

    def kill_pacman(surface,sound,ghost):
        pass