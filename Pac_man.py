from ast import Pass
from ScreenType import ScreenType
import pygame

from pygame.cursors import tri_left

from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL,K_ESCAPE)

from pellet import Pellet

class Pac_man(pygame.sprite.Sprite):
    def __init__(self, maxHeight, maxWidth, screen, map):
        self.dic = {"right": True, "left": True, "top": True, "bottom": True}
        self.map = map
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth
        super(Pac_man, self).__init__()
        image = "./Assets/Sprites/Pac_mans/Right_open.png"
        self.surf = pygame.image.load(image).convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (280,465)
        )
        self.speed = 1
        screen.blit(self.surf,self.rect)
        self.chompSound = pygame.mixer.Sound("./Assets/Music/pacman_chomp.wav")
            



    def pac_right(self, d, amount):
        if self.dic["right"] == True:
            if d == "d":
                self.rect.centerx += amount
                image = "./Assets/Sprites/Pac_mans/Right_open.png"
                self.surf = pygame.image.load(image).convert_alpha()
        else:
            self.dic["right"] = False
    def pac_left(self, a, amount):
        if self.dic["left"] == True:
            if a == "a":
                self.rect.centerx -= amount
                image = "./Assets/Sprites/Pac_mans/Left_open.png"
                self.surf = pygame.image.load(image).convert_alpha()
        else:
            self.dic["left"] = False
    def pac_down(self, s, amount):
        if self.dic["bottom"] == True:
            if s == "s":
                self.rect.centery += amount
                image = "./Assets/Sprites/Pac_mans/Down_open.png"
                self.surf = pygame.image.load(image).convert_alpha()
        else:
            self.dic["bottom"] = False
    def pac_up(self, w, amount):
        self.check_wall(0)
        if w == "w":
            self.rect.centery -= amount
            image = "./Assets/Sprites/Pac_mans/Up_open.png"
            self.surf = pygame.image.load(image).convert_alpha()
        else:
            self.dic["top"] = False

    def move_pacman(self, kd):
        if len(pygame.sprite.spritecollide(self, self.map.walls, False)) == 0:
            self.pac_right(kd, 5)
            self.pac_left(kd, 5)
            self.pac_up(kd, 5)
            self.pac_down(kd, 5)
        
        else:
            pass
            



    def kill_pacman(surface,sound,ghost):
        pass

    def chomp(self):
        pygame.mixer.Sound.play(self.chompSound)

    def eat(self):
        if len(pygame.sprite.spritecollide(self, self.map.pellets, True)) > 0:
            self.chomp()