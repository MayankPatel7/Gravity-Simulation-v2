import pygame
from sys import exit

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Flight Simulator")
clock = pygame.time.Clock()
FPS = 100

running = True
while(running):
    screen.fill((50, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
exit()