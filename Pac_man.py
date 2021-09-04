import pygame, sys, turtle




pygame.init()
sw = 576
sh = 448
screen = pygame.display.set_mode((sw,sh))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

        screen.fill((0,0,0))