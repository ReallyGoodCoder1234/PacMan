import pygame, sys, random
from Direction import Direction
from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL)

class Ghost(pygame.sprite.Sprite):
    directions = [Direction.Forward, Direction.Backward, Direction.Up, Direction.Down]
    directionImage = ["right", "left", "forward", "forward"]

    def __init__(self, name, pos, maxHeight, maxWidth, map):
        self.name = name
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth
        super(Ghost, self).__init__()
        self.direction = random.choice(self.directions)
        image = "./Assets/Sprites/Ghosts/" + self.name + "/" + self.name + "_" + self.directionImage[int(self.direction)] + ".png"
        self.surf = pygame.image.load(image).convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = pos
        )
        self.speed = 2
        self.map = map

    def update(self):
        if self.direction == Direction.Forward:
            self.rect.centerx += self.speed
            for r in self.map.walls:
                if self.rect.colliderect(r):
                    self.rect.centerx -= self.speed
                    self.direction = random.choice(self.directions)
        elif self.direction == Direction.Backward:
            self.rect.centerx -= self.speed
            for r in self.map.walls:
                if self.rect.colliderect(r):
                    self.rect.centerx += self.speed
                    self.direction = random.choice(self.directions)
        elif self.direction == Direction.Up:
            self.rect.centery -= self.speed
            for r in self.map.walls:
                if self.rect.colliderect(r):
                    self.rect.centery += self.speed
                    self.direction = random.choice(self.directions)
        else:
            self.rect.centery += self.speed
            for r in self.map.walls:
                if self.rect.colliderect(r):
                    self.rect.centery -= self.speed
                    self.direction = random.choice(self.directions)

        if self.rect.left <= 0:
            self.direction = Direction.Forward
        if self.rect.right > self.maxWidth:
            self.direction = Direction.Backward
        if self.rect.top <= 0:
            self.direction = Direction.Down
        if self.rect.bottom >= self.maxHeight:
            self.direction = Direction.Up

        image = "./Assets/Sprites/Ghosts/" + self.name + "/" + self.name + "_" + self.directionImage[int(self.direction)] + ".png"
        self.surf = pygame.image.load(image).convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)

    def release_ghost():
        pass
