import pygame

class MapCreator(pygame.sprite.Sprite):

    def __init__(self):
        self.world = []
        self.walldic = {'.': './Assets/Levels_and_backgrounds/pellet.png', '=': './Assets/Levels_and_backgrounds/pellet.png', '*': 'power.png',}

    def download_level(self, file):
        with open(file) as f:
            for line in f:
                row = []
                for block in line:
                    row.append(block)
                self.world.append(row)

    def draw_image(self, screen, bs):
        for y, row in enumerate(self.world):
            for x, block in enumerate(row):
                image = self.walldic.get(block, None)
                if image:
                    im = pygame.image.load(self.walldic[block]).convert_alpha()
                    screen.blit(im, (x*bs, y*bs))