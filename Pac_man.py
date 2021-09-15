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

sw = 500
sh = 500
screen = pygame.display.set_mode((sw,sh))

# Pac man
pac_man_surface = pygame.image.load("./Assets/Sprites/Pac_mans/Left_open.png").convert_alpha()
pac_man_rect = pac_man_surface.get_rect()



# Game Variables
ghost_amount = 0
ghost_colours = []

# Buttons
quit_button = Button('Quit',200,40,(25,450),6)
credits_button = Button('Credits',200,40,(25,350),6)
how_button = Button('How To Play',200,40,(275,450),6)
play_button = Button('Play',200,40,(275,350),6)

# Backgrounds
main_menu_background = pygame.transform.scale2x(pygame.image.load("./Assets/Levels_and_backgrounds/Main_menu_backgound.png"))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or quit_button.pressed == True:
           print("quit") 
           pygame.quit()
           sys.exit()
        elif play_button.pressed == True:
            sw = 1428 
            sh = 598
            screen = pygame.display.set_mode((sw,sh))
        else:
            screen.blit(main_menu_background,(0,0))
            quit_button.draw(screen)
            credits_button.draw(screen)
            how_button.draw(screen)
            play_button.draw(screen)
        #if event.type == pygame.KEYDOWN:
        #    move_pacman(pac_man_surface)
        #elif event.type == ADDGHOST:
           # if ghost_amount < 4:
          #      ghost = Ghost()
         #       all_sprites.add(ghost)
        #    ghost_amount += 1
       # elif event.type == RELEASEGHOST:
      #      release_ghost()
    


    # Fill screen with black
    screen.blit(main_menu_background,(0,0))
    quit_button.draw(screen)
    credits_button.draw(screen)
    how_button.draw(screen)
    play_button.draw(screen)
    #screen.blit(pac_man_surface,(200,200))
    # Draw all ghosts
    #for entity in all_sprites:
     #   screen.blit(entity.surf, entity.rect)
    
    pygame.display.flip()