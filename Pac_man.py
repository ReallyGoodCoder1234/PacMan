import pygame, sys, random
from Buttons import Button

from pygame.locals import (K_DOWN, K_UP, K_UP, K_LEFT, K_RIGHT, K_a, K_d, K_s, K_w, RLEACCEL)

class Ghost(pygame.sprite.Sprite):
    global ghost_colours
    def __init__(self):
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

def move_pacman(self):
    if K_LEFT == True:
        self = pygame.image.load("./Assets/Sprites/Pac_mans/Right_open.png").convert_alpha()
        self.rect.move_ip(-5, 0)
    elif K_UP == True:
        self = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
        self.rect.move_ip(0, -5)
    elif K_DOWN == True:
        self = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
        self.rect.move_ip(0, 5)
    elif K_RIGHT == True:
        self = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()  
        self.rect.move_ip(5, 0)
   
def kill_pacman(surface,sounde,ghost):
    pass

pygame.init()

ghost_list = ["Blue", "Grey", "Orange", "Pink", "Red", "White"]
all_sprites = pygame.sprite.Group()

ADDGHOST = pygame.USEREVENT + 1
pygame.time.set_timer(ADDGHOST, 1200)

RELEASEGHOST = pygame.USEREVENT + 1
pygame.time.set_timer(RELEASEGHOST, 5500)

pygame.display.set_caption('Main Menu')

# Pac man
pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
pac_man_rect = pac_man_surface.get_rect()

sw = 1428
sh = 598
screen = pygame.dislpay.set_mode((sw,sh))

# Game Variables
ghost_amount = 0
ghost_colours = []

# Buttons
button1 = Button('Quit',200,40,(25,450),6)
button2 = Button('Credits',200,40,(25,350),6)
button3 = Button('How To Play',200,40,(275,450),6)
button4 = Button('Play',200,40,(275,350),6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or quit == True:
            pygame.quit()
            sys.exit()
        elif play == True:
            if event.type == pygame.KEYDOWN:
                move_pacman(pac_man_surface)
            elif event.type == ADDGHOST:
                if ghost_amount < 4:
                    ghost = Ghost()
                    all_sprites.add(ghost)
                ghost_amount += 1
            elif event.type == RELEASEGHOST:
                release_ghost()

    button1.draw()
    button2.draw()
    button3.draw()
    button4.draw()

    # Fill screen with black
    screen.fill((0, 0, 0))

    screen.blit(pac_man_surface,(200,200))
    # Draw all ghosts
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    pygame.display.flip()