import pygame, random
from Ghost import Ghost

class GhostManager(pygame.sprite.Sprite):
    name_list = ["Blue", "Grey", "Orange", "Pink", "Red", "White"]
    ghosts = pygame.sprite.Group()

    def __init__(self, maxHeight, maxWidth):
        super().__init__()
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth

    def createGhost(self):
        # only create max to 4 ghosts
        if len(self.ghosts) >= 5:
            return
        
        # do not create with same color
        while True:
            name = random.choice(self.name_list)
            existing = [n for n in self.ghosts.sprites() if n.name == name]
            if len(existing) == 0:
                break

        ghost = Ghost(name, (random.randint(0, self.maxHeight), random.randint(0, self.maxWidth)), self.maxHeight, self.maxWidth)
        self.ghosts.add(ghost)
        return ghost
    
    def killGhost(self, ghost):
        pass
