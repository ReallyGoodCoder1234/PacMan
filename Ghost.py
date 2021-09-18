import pygame, sys, random
from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL)

class Ghost(pygame.sprite.Sprite):
    ghost_list = ["Blue", "Grey", "Orange", "Pink", "Red", "White"]
    ghost_name = ""

    def __init__(self, pos):
        super(Ghost, self).__init__()
        self.ghost_name = random.choice(self.ghost_list)
        image = "./Assets/Sprites/Ghosts/" + self.ghost_name + "/" + self.ghost_name + "_forward.png"
        print(image)
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = pos
        )

    def release_ghost():
        pass
