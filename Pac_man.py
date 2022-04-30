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

    def eat(self):
        if len(pygame.sprite.spritecollide(self, self.map.pellets, True)) > 0:
            self.chomp()

    def pac_right(self, d, amount, i):
        if d == "d":
            while i == 0:
                self.rect.centerx += amount
                image = "./Assets/Sprites/Pac_mans/Right_open.png"
                self.surf = pygame.image.load(image).convert_alpha()
                self.eat()
                for r in self.map.walls:
                    if self.rect.colliderect(r):
                        self.rect.centerx -= amount
                        i = 1


    def pac_left(self, a, amount, i):
        if a == "a":
            while i == 0:
                self.rect.centerx -= amount
                self.eat()
                image = "./Assets/Sprites/Pac_mans/Left_open.png"
                self.surf = pygame.image.load(image).convert_alpha()
                for r in self.map.walls:
                    if self.rect.colliderect(r):
                        self.rect.centerx += amount
                        i = 1

    def pac_down(self, s, amount, i):
        if s == "s":
            while i == 0:
                self.rect.centery += amount
                self.eat()
                image = "./Assets/Sprites/Pac_mans/Down_open.png"
                self.surf = pygame.image.load(image).convert_alpha()
                for r in self.map.walls:
                    if self.rect.colliderect(r):
                        self.rect.centery -= amount
                        i = 1
    def pac_up(self, w, amount, i):
        if w == "w":
            while i == 0:
                self.rect.centery -= amount
                self.eat()
                image = "./Assets/Sprites/Pac_mans/Up_open.png"
                self.surf = pygame.image.load(image).convert_alpha()
                for r in self.map.walls:
                    if self.rect.colliderect(r):
                        self.rect.centery += amount
                        i = 1

    def move_pacman(self, kd, i):
        self.pac_right(kd, 1, i)
        self.pac_left(kd, 1, i)
        self.pac_up(kd, 1, i)
        self.pac_down(kd, 1, i)

    def kill_pacman(surface,sound,ghost):
        pass

    def chomp(self):
        pygame.mixer.Sound.play(self.chompSound)