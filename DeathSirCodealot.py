import pygame

class SirCodealot(pygame.sprite.Sprite):
    def __init__(self, height, width):
        super(SirCodealot, self).__init__()
        image = "Assets/Levels_and_backgrounds/FaceRight.png"
        self.surf = pygame.image.load(image).convert_alpha()
        pygame.transform.scale2x(self.surf)
        self.rect = self.surf.get_rect(
            center = (width // 2, height // 2)
        )