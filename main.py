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
TIME_SCALE = 1

craft = spacecraft.Spacecraft(1, 340, 360, 0, -900)
earth = planet.Planet(50000, 440, 360, 64, "earth.png")

running = True
while(running):
    dt = (clock.tick(FPS)/1000)*TIME_SCALE
    screen.fill((50, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(earth.surface, earth.pos)
    earth.update()

    for i, point in enumerate(craft.trail):
        alpha = int(255 * i / len(craft.trail))  # fade older points
        pygame.draw.circle(screen, (255, 255, alpha), point, 1)

    craft.gravity(earth)
    craft.update(dt)
    screen.blit(craft.surface, craft.pos)

    pygame.display.update()
pygame.quit()
exit()