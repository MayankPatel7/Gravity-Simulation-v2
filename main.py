import pygame
import spacecraft
import planet
import math
from sys import exit

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravity Simulation v2")
clock = pygame.time.Clock()
FPS = 100
TIME_SCALE = 1

stats_font = pygame.font.Font(None, 32)

craft = spacecraft.Spacecraft(1, 640, 160, 500, 0)
earth = planet.Planet(50000, 640, 360, 64, "earth.png")

running = True
while(running):
    dt = (clock.tick(FPS)/1000)*TIME_SCALE
    screen.fill((50, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PERIOD:
                TIME_SCALE += 0.5
            if event.key == pygame.K_COMMA:
                TIME_SCALE -= 0.5
            if(event.key == pygame.K_o):
                craft.orbital_vel(earth)
            if event.key == pygame.K_UP: craft.velY -= 5
            elif event.key == pygame.K_DOWN: craft.velY += 5

            if event.key == pygame.K_RIGHT: craft.velX += 5
            elif event.key == pygame.K_LEFT: craft.velX -= 5

    screen.blit(earth.surface, earth.pos)
    earth.update()

    for i, point in enumerate(craft.trail):
        alpha = int(255 * i / len(craft.trail))
        pygame.draw.circle(screen, (alpha, 255, 255), point, 1)

    craft.gravity(earth)
    craft.update(dt)
    screen.blit(craft.surface, craft.pos)

    stats = f"Apogee: {str(craft.apogee)}\nPerigee: {str(craft.perigee)}\nAltitude: {str(craft.altitude)}\nVelocity: {str(int(math.sqrt(craft.velX**2 + craft.velY**2)))} px/s"
    stats_text_surface = stats_font.render(stats, True, (255, 255, 255))
    timescale_text_surface = stats_font.render(f"x{str(TIME_SCALE)}", True, (255, 255, 255))
    screen.blit(stats_text_surface, (10, 10))
    screen.blit(timescale_text_surface, (630, 10))

    pygame.display.update()
pygame.quit()
exit()