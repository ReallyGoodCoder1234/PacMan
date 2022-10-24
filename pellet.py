import pygame

class Pellet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Pellet, self).__init__()
        image = "./Assets/Levels_and_backgrounds/Gear.png"
        self.surf = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect(
            center = (x+4, y+4)
        )

    def remove(self, group):
        group.remove_internal(self)

    def update(self):
        image = "./Assets/Levels_and_backgrounds/Gear.png"
        self.surf = pygame.image.load(image).convert_alpha()