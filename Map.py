import pygame

class MapCreator(pygame.sprite.Sprite):

    def __init__(self):
        self.worldwall = []
        self.worldpellet = []
        self.worldpower = []
        self.worldgate = []
        
        self.walldic = {'.': pygame.image.load("./Assets/Levels_and_backgrounds/Pellet.png"), '=': pygame.image.load("./Assets/Levels_and_backgrounds/Wall.png"), '*': pygame.image.load('./Assets/Levels_and_backgrounds/Power_Pellet.png'), '-': pygame.image.load('./Assets/Levels_and_backgrounds/Door.png')}
        self.walllist = []
        self.pelletlist = []
        self.powerlist = []
        self.gatelist = []

    def download_level(self, walls, pellets, gate, power):
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

        with open(gate) as g:
            for line in g:
                row = []
                for block in line:
                    row.append(block)
                self.worldgate.append(row)

    def draw_walls(self, screen, bs):
        for y, row in enumerate(self.worldwall):
            for x, block in enumerate(row):
                image = self.walldic.get(block, None)
                if image:
                    screen.blit(self.walldic.get('='), (x*bs, y*bs))
                    self.walllist.append([x*bs, y*bs])

    def draw_pellets(self, screen, bs):
        for y, row in enumerate(self.worldpellet):
            for x, block in enumerate(row):
                image = self.walldic.get(block, None)
                if image:
                    screen.blit(self.walldic.get('.'), (x*bs, y*bs))
                    self.pelletlist.append([x*bs, y*bs])

    def draw_gate(self, screen, bs):
        for y, row in enumerate(self.worldpower):
            for x, block in enumerate(row):
                image = self.walldic.get(block, None)
                if image:
                    screen.blit(self.walldic.get('-'), (x*bs, y*bs))
                    self.gatelist.append([x*bs, y*bs])