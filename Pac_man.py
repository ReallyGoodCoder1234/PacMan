from ScreenType import ScreenType
import pygame, sys, random

from pygame.cursors import tri_left

from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL,K_ESCAPE)

class Pac_man(pygame.sprite.Sprite):
    def __init__(self, maxHeight, maxWidth, screen, map):
        self.map = map
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth
        super(Pac_man, self).__init__()
        image = "./Assets/Sprites/Pac_mans/Right_open.png"
        self.surf = pygame.image.load(image).convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.speed = 1
        screen.blit(self.surf,self.rect)

    def pac_right(self, d, amount):
        if d == "d":
            self.rect.centerx += amount
            image = "./Assets/Sprites/Pac_mans/Right_open.png"
            self.surf = pygame.image.load(image).convert_alpha()
    def pac_left(self, a, amount):
        if a == "a":
            self.rect.centerx -= amount
            image = "./Assets/Sprites/Pac_mans/Left_open.png"
            self.surf = pygame.image.load(image).convert_alpha()
    def pac_down(self, s, amount):
        if s == "s":
            self.rect.centery += amount
            image = "./Assets/Sprites/Pac_mans/Down_open.png"
            self.surf = pygame.image.load(image).convert_alpha()            
    def pac_up(self, w, amount):
        if w == "w":
            self.rect.centery -= amount
            image = "./Assets/Sprites/Pac_mans/Up_open.png"
            self.surf = pygame.image.load(image).convert_alpha()            

    def move_pacman(self, kd):
        self.pac_right(kd, 5)
        self.pac_left(kd, 5)
        self.pac_up(kd, 5)
        self.pac_down(kd, 5)

    def kill_pacman(surface,sound,ghost):
        pass

    def collide_wall(self):
        for wall in self.map.walllist:
            wallr = wall.get_rect
            if self.rect.top < wallr.bottom:
                self.rect.top = wallr.bottom

            if self.rect.bottom > wallr.top:
                self.rect.bottom = wallr.top

            if self.rect.right > wallr.left:
                self.rect.right = wallr.left

            if self.rect.left < wallr.right:
                self.rect.left = wallr.right
    
    def eat(self):
        for pellet in self.map.pelletlist:
            if self.rect.colliderect(pellet.rect):
                pygame.sprite.Sprite.kill(pellet)