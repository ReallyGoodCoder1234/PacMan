import pygame, random
from Ghost import Ghost

class GhostManager(pygame.sprite.Sprite):
    name_list = ["Blue", "Grey", "Orange", "Pink", "Red", "White"]
    ghosts = pygame.sprite.Group()

    def __init__(self, maxHeight, maxWidth):
        super().__init__()
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth

    def createGhost(self, map):
        # only create max to 4 ghosts
        if len(self.ghosts) >= 4:
            return
        
        ghost = Ghost((220,225), self.maxHeight, self.maxWidth, map)
        self.ghosts.add(ghost)
        return ghost
    
    def killGhost(self, ghost):
        pass
