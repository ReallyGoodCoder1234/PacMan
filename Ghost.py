import pygame, sys, random
from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL)

Direction_Forward = 1
Direction_Backward = 2
Direction_Up = 3
Direction_Down = 4

class Ghost(pygame.sprite.Sprite):
    directions = ["forward", "back", "left", "right"]

    def __init__(self, name, pos, maxHeight, maxWidth):
        self.name = name
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth
        super(Ghost, self).__init__()
        self.direction = random.choice(self.directions)
        image = "./Assets/Sprites/Ghosts/" + self.name + "/" + self.name + "_" + self.direction + ".png"
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = pos
        )
        self.speed = 1

    def update(self):
        if self.direction == "forward":
            self.rect.move_ip(self.speed, 0)
        elif self.direction == "back":
            self.rect.move_ip(-self.speed, 0)
        elif self.direction == "left":
            self.rect.move_ip(0, self.speed)
        else:
            self.rect.move_ip(0, -self.speed)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.maxWidth:
            self.rect.right = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.maxHeight:
            self.rect.bottom = 0

    def release_ghost():
        pass
