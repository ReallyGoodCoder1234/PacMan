from ScreenType import ScreenType
import pygame, sys, random

from pygame.cursors import tri_left

from pygame import mixer

from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL,K_ESCAPE)

from pellet import Pellet

class Pac_man(pygame.sprite.Sprite):
    def __init__(self, maxHeight, maxWidth, screen, map):
        self.dic = {"right": False, "left": False, "top": False, "bottom": False}
        self.map = map
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth
        super(Pac_man, self).__init__()
        image = "./Assets/Sprites/Pac_mans/Right_open.png"
        self.surf = pygame.image.load(image).convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (280,470)
        )
        self.speed = 1
        screen.blit(self.surf,self.rect)

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
        if self.dic["top"] == True:
            if w == "w":
                self.rect.centery -= amount
                image = "./Assets/Sprites/Pac_mans/Up_open.png"
                self.surf = pygame.image.load(image).convert_alpha()
        else:
            self.dic["top"] = False

    def move_pacman(self, kd):

        self.pac_right(kd, 5)
        self.pac_left(kd, 5)
        self.pac_up(kd, 5)
        self.pac_down(kd, 5)


    def kill_pacman(surface,sound,ghost):
        pass

    def check_wall(self):
        if len(pygame.sprite.spritecollide(self,self.map.walls,False, None)) >= 1:
            collidelist = pygame.sprite.spritecollide(self, self.map.walls, False, None)
            for x in collidelist:
                if self.rect.left >= x.rect.right:
                    self.dic["right"] = True
                elif self.rect.right <= x.rect.left:
                   self.dic["left"] = True
                elif self.rect.top <= x.rect.bottom:
                   self.dic["top"] = True
                elif self.rect.bottom >= x.rect.top:
                   self.dic["bottom"] = True
                else:
                    self.dic = {"right": False, "left": False, "top": False, "bottom": False}

    def chomp():
        mixer.init()
        mixer.music.load("./Assets/Music/pacman_chomp.wav")
        mixer.music.set_volume(100)
        mixer.music.play()

    def eat(self):
        if len(pygame.sprite.spritecollide(self, self.map.pellets, True)) >= 1:
            die = pygame.sprite.spritecollide(self, self.map.pellets, True)
            for x in die:
                self.map.pellets.remove(x)
                Pac_man.chomp()
        else:
            return False

