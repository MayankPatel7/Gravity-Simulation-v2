import pygame
import spacecraft
import planet
from sys import exit

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Flight Simulator")
clock = pygame.time.Clock()
FPS = 100

craft = spacecraft.Spacecraft(1000, 640, 160, 0, 0)
earth = planet.Planet(6*(10**24), 640, 360, 64)

running = True
while(running):
    screen.fill((50, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    
    screen.blit(earth.surface, earth.pos)
    earth.update()

    screen.blit(craft.surface, craft.pos)
    craft.update()

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
exit()