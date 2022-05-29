import pygame
import GLOBABAL

from pygame.locals import (RLEACCEL)


class Pac_man(pygame.sprite.Sprite):
    def __init__(self, maxHeight, maxWidth, screen, map):
        self.direction = "right"
        self.collides = {"up":False, "down":False, "left":False, "right":False}
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
            GLOBABAL.score += 10


    def pac_right(self, amount):
        if self.collides.get("right") == False:
            self.rect.centerx += amount
            image = "./Assets/Sprites/Pac_mans/Right_open.png"
            self.surf = pygame.image.load(image).convert_alpha()
            self.eat()
            for r in self.map.walls:
                if self.rect.colliderect(r):
                    self.rect.centerx -= amount
                    self.collides.update({"right": True})
            self.collides.update({"right": False})
        


    def pac_left(self, amount):
        if self.collides.get("left") == False:
            self.rect.centerx -= amount
            self.eat()
            image = "./Assets/Sprites/Pac_mans/Left_open.png"
            self.surf = pygame.image.load(image).convert_alpha()
            for r in self.map.walls:
                if self.rect.colliderect(r):
                    self.rect.centerx += amount
                    self.collides.update({"left": True})
            self.collides.update({"left": False})
            

    def pac_down(self, amount):
        if self.collides.get("down") == False:
            self.rect.centery += amount
            self.eat()
            image = "./Assets/Sprites/Pac_mans/Down_open.png"
            self.surf = pygame.image.load(image).convert_alpha()
            for r in self.map.walls:
                if self.rect.colliderect(r):
                    self.rect.centery -= amount
                    self.collides.update({"down": True})
            self.collides.update({"down": False})


    def pac_up(self, amount):
        if self.collides.get("up") == False:
            self.rect.centery -= amount
            self.eat()
            image = "./Assets/Sprites/Pac_mans/Up_open.png"
            self.surf = pygame.image.load(image).convert_alpha()
            for r in self.map.walls:
                if self.rect.colliderect(r):
                    self.rect.centery += amount
                    self.collides.update({"up": True})
            self.collides.update({"up": False})



    def move_pacman(self):
        if self.direction == "right":
            self.pac_right(3)
        if self.direction == "left":
            self.pac_left(3)
        if self.direction == "up":
            self.pac_up(3)
        if self.direction == "down":
            self.pac_down(3)

    def kill_pacman(surface,sound,ghost):
        pass

    def chomp(self):
        pygame.mixer.Sound.play(self.chompSound)