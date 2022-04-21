import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Wall, self).__init__()
        image = "./Assets/Levels_and_backgrounds/Wall.png"
        self.surf = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect(
            center = (x, y)
        )

    def update(self):
        image = "./Assets/Levels_and_backgrounds/Wall.png"
        self.surf = pygame.image.load(image).convert_alpha()