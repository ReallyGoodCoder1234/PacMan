import pygame
from msilib.schema import Class

class MapCreator(pygame.sprite.Sprite):

    def __init__(self):
        self.world = []
        self.file = open("Map1.txt")
        self.walldic = {'.': 'dot.png', '=': 'wall.png', '*': 'power.png',}

    def download_level(self):
        with open(self.file) as f:
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
                    screen.blit(self.walldic[block], (x*bs, y*bs))