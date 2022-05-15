import pygame

from pygame.locals import (RLEACCEL)


class Pac_man(pygame.sprite.Sprite):
    def __init__(self, maxHeight, maxWidth, screen, map):
        self.direction = "right"
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

    def pac_right(self, amount):
        self.rect.centerx += amount
        image = "./Assets/Sprites/Pac_mans/Right_open.png"
        self.surf = pygame.image.load(image).convert_alpha()
        self.eat()
        for r in self.map.walls:
            if self.rect.colliderect(r):
                self.rect.centerx -= amount


    def pac_left(self, amount):
        self.rect.centerx -= amount
        self.eat()
        image = "./Assets/Sprites/Pac_mans/Left_open.png"
        self.surf = pygame.image.load(image).convert_alpha()
        for r in self.map.walls:
            if self.rect.colliderect(r):
                self.rect.centerx += amount

    def pac_down(self, amount):
        self.rect.centery += amount
        self.eat()
        image = "./Assets/Sprites/Pac_mans/Down_open.png"
        self.surf = pygame.image.load(image).convert_alpha()
        for r in self.map.walls:
            if self.rect.colliderect(r):
                self.rect.centery -= amount

    def pac_up(self, amount):
        self.rect.centery -= amount
        self.eat()
        image = "./Assets/Sprites/Pac_mans/Up_open.png"
        self.surf = pygame.image.load(image).convert_alpha()
        for r in self.map.walls:
            if self.rect.colliderect(r):
                self.rect.centery += amount

    def move_pacman(self):
        if self.direction == "right":
            self.pac_right(3)
        elif self.direction == "left":
            self.pac_left(3)
        elif self.direction == "up":
            self.pac_up(3)
        elif self.direction == "down":
            self.pac_down(3)

    def kill_pacman(surface,sound,ghost):
        pass

    def chomp(self):
        pygame.mixer.Sound.play(self.chompSound)