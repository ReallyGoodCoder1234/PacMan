import pygame

sw = 500
sh = 500
screen = pygame.display.set_mode((sw,sh))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.toggle_fullscreen()