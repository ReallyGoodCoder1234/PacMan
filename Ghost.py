import pygame, sys, random
from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL)

class Ghost(pygame.sprite.Sprite):
    global ghost_colours
    def __init__(self):
        ghost_list = ["Blue", "Grey", "Orange", "Pink", "Red", "White"]
        all_sprites = pygame.sprite.Group()
        ADDGHOST = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDGHOST, 1200)
        RELEASEGHOST = pygame.USEREVENT + 1
        pygame.time.set_timer(RELEASEGHOST, 5500)
        ghost_amount = 0
        ghost_colours = []

        super(Ghost, self).__init__()
        imageName = random.choice(ghost_list)
        while ghost_colours.count(imageName) != 0:
           imageName = random.choice(ghost_list)

        self.surf = pygame.image.load("./Assets/Sprites/Ghosts/" + imageName + "/" + imageName + "_forward.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        ghost_colours.append(imageName)
        self.rect = self.surf.get_rect(
            center = (
                714,
                299
            )
        )

    def release_ghost():
        pass
