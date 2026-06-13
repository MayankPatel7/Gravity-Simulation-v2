import pygame
import math

G = 1000

class Spacecraft(pygame.sprite.Sprite):
    def __init__(self, mass, x, y, velX, velY):
        super().__init__()
        self.surface = pygame.Surface((15, 15))
        self.surface.fill((33, 255, 248))
        self.pos = self.surface.get_rect(center = (x, y))
        self.velX = velX
        self.velY = velY
        self.accX = 0
        self.accY = 0
        self.mass = mass
        self.x = float(x)  # float position
        self.y = float(y)
        self.trail = []
        self.trail_length = 500

    def gravity(self, planet):
        dx = planet.pos.centerx - self.pos.centerx
        dy = planet.pos.centery - self.pos.centery
        r = math.sqrt((dx**2 + dy**2))
        force = (G*planet.mass*self.mass)/r**2
        self.accX += (force/self.mass)*(dx/r)
        self.accY += (force/self.mass)*(dy/r)

    def update(self, dt):
        self.velX += self.accX * dt
        self.velY += self.accY * dt
        self.x += self.velX * dt  # update floats
        self.y += self.velY * dt
        self.pos.centerx = int(self.x)  # only convert to int for drawing
        self.pos.centery = int(self.y)

        self.trail.append((self.pos.centerx, self.pos.centery))
        # if len(self.trail) > self.trail_length:
        #     self.trail.pop(0)

        self.accY = 0
        self.accX = 0