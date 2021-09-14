import pygame, sys, random

from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL)

class Ghost(pygame.sprite.Sprite):
    def __init__(self):
        super(Ghost, self).__init__()
        imageName = random.choice(ghost_list)
        image = "./Assets/Sprites/Ghosts/" + imageName + "/" + imageName + "_forward.png"
        print(image)
        self.surf = pygame.image.load(image).convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center = (
                random.randint(0, sw),
                random.randint(0, sh)
            )
        )
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= sh:
            self.rect.bottom = sh

def move_pacman():
    if K_a == True:
        pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Right_open.png").convert_alpha()
        pac_man_surface.centerx -= 1
    elif K_w == True:
        pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
        pac_man_surface.centery -= 1
    elif K_s == True:
        pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
        pac_man_surface.centery += 1
    elif K_d == True:
        pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
        pac_man_surface.centerx += 1
        

pygame.init()

ghost_list = ["Blue", "Grey", "Orange", "Pink", "Red", "White"]
all_sprites = pygame.sprite.Group()

ADDGHOST = pygame.USEREVENT + 1
pygame.time.set_timer(ADDGHOST, 1200)

# Pac man
#pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
#pac_man_rect = pac_man_surface.get_rect()

sw = 1427
sh = 598
screen = pygame.display.set_mode((sw,sh))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            move_pacman()
        elif event.type == ADDGHOST:
            ghost = Ghost()
            all_sprites.add(ghost)

    # Fill screen with black
    screen.fill((0, 0, 0))

    # Draw all ghosts
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    pygame.display.flip()