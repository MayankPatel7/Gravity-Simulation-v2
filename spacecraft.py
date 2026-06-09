import pygame

G = 6.67*(10**-11)

class Spacecraft(pygame.sprite.Sprite):
    def __init__(self, mass, x, y, velX, velY):
        super().__init__()
        self.surface = pygame.Surface((15, 15))
        self.pos = self.surface.get_rect(center = (x, y))
        self.velX = velX
        self.velY = velY
        self.accX = 0
        self.accY = 0
        self.mass = mass

    def update(self):
        self.surface.fill((33, 255, 248))
        self.velX += self.accX
        self.velY += self.accY
        self.pos.x += self.velX
        self.pos.y += self.velY