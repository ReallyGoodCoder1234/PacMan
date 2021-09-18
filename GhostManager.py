import pygame, random
from Ghost import Ghost

class GhostManager(pygame.sprite.Sprite):
    ghost_names = []
    ghosts = []

    def __init__(self):
        super().__init__()

    def createGhost(self):
        # only create max to 4 ghosts
        if len(self.ghosts) >= 4:
            return
        
        ghost = Ghost((random.randint(0, 100), random.randint(0, 100)))
        self.ghosts.append(ghost)
        return ghost
    
    def killGhost(self, ghost):
        pass
