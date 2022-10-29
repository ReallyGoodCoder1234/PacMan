import pygame

class Power(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Power, self).__init__()
        image = "./Assets/Levels_and_backgrounds/Robot1Head02.png"
        self.surf = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect(
            center = (x, y)
        )

    def remove(self, group):
        group.remove_internal(self)

    def update(self):
        image = "./Assets/Levels_and_backgrounds/Robot1Head02.png"
        self.surf = pygame.image.load(image).convert_alpha()