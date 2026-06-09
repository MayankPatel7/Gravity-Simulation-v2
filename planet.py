import pygame

class Planet(pygame.sprite.Sprite):
    def __init__(self, mass, x, y, radius):
        super().__init__()
        self.surface = pygame.Surface((radius*2, radius*2))
        self.pos = self.surface.get_rect(center = (x, y))
        self.mass = mass
        self.radius = radius

    def update(self):
        self.surface.fill((33, 255, 248))