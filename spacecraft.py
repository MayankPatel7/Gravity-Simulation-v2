import pygame

class Spacecraft(pygame.sprite.Sprite):
    def __init__(self, mass, x, y, velX, velY):
        self.surface = pygame.Surface((50, 50))
        self.pos = pygame.rect(center = (x, y))
        self.velX = velX
        self.velY = velY
        self.mass = mass

    def update(self):
        self.pos.x += self.velX
        self.pos.y += self.velY