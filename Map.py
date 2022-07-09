import pygame
from pellet import Pellet
from wall import Wall
from Power import Power

class MapCreator(pygame.sprite.Sprite):

    def __init__(self):
        self.worldwall = []
        self.worldpellet = []
        self.worldpower = []
        self.worldgate = []
        
        self.walldic = {'.': "./Assets/Levels_and_backgrounds/Pellet.png", '=': "./Assets/Levels_and_backgrounds/Wall.png", '*': './Assets/Levels_and_backgrounds/Power_Pellet.png', '-': './Assets/Levels_and_backgrounds/Door.png'}
        self.walllist = []
        self.pellets = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.power = pygame.sprite.Group()

    def download_level(self, walls, pellets, power):
        with open(walls) as w:
            for line in w:
                row = []
                for block in line:
                    row.append(block)
                self.worldwall.append(row)

        with open(pellets) as p:
            for line in p:
                row = []
                for block in line:
                    row.append(block)
                self.worldpellet.append(row)

        with open(power) as po:
            for line in po:
                row = []
                for block in line:
                    row.append(block)
                self.worldpellet.append(row)

    def create_walls(self):
        for y, row in enumerate(self.worldwall):
            for x, block in enumerate(row):
                imageFile = self.walldic.get(block, None)
                if imageFile:
                    wall = Wall(x*20+5, y*20+5)
                    self.walls.add(wall)

    def create_pellet(self):
        for y, row in enumerate(self.worldpellet):
            for x, block in enumerate(row):
                imageFile = self.walldic.get(block, None)
                if imageFile:
                    pellet = Pellet(x*20+5, y*20+5)
                    self.pellets.add(pellet)

    def create_power(self):
        for y, row in enumerate(self.worldpower):
            for x, block in enumerate(row):
                imageFile = self.walldic.get(block, None)
                if imageFile:
                    power = Power(x*20+5, y*20+5)
                    self.powers.add(power)

    def draw_gate(self, screen, bs):
        self.draw_map(screen, bs, 0, self.worldpower, self.gatelist)

    def draw_map(self, screen, bs, offset, objectMap, objectList):
        for y, row in enumerate(objectMap):
            for x, block in enumerate(row):
                imageFile = self.walldic.get(block, None)
                if imageFile:
                    image = pygame.image.load(imageFile)
                    screen.blit(image, (x*bs+offset, y*bs+offset))
                    objectList.append(image)