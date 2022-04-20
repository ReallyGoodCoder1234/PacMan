import pygame
from pygame.locals import (RLEACCEL)

class Pellet(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(Pellet, self).__init__()
        image = "./Assets/Levels_and_backgrounds/Pellet.png"
        self.surf = pygame.image.load(image).convert_alpha()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        screen.blit(self.surf, (x, y))