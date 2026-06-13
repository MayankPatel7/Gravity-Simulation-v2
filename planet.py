import pygame

class Planet(pygame.sprite.Sprite):
    def __init__(self, mass, x, y, radius, texture_path):
        super().__init__()
        self.raw = pygame.image.load(texture_path).convert_alpha()
        self.surface = pygame.transform.scale(self.raw, (radius*2, radius*2))
        self.pos = self.surface.get_rect(center = (x, y))
        self.mass = mass
        self.radius = radius

    def update(self):
        pass