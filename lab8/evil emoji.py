import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# Initialing RGB Color
color = (255, 255, 255)
screen.fill(color)
pygame.display.flip()

circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
circle(screen, (255, 0, 0), (150, 185), 20)
circle(screen, (255, 0, 0), (250, 185), 30)
circle(screen, (0, 0, 0), (250, 185), 30, 1)
circle(screen, (0, 0, 0), (150, 185), 20, 1)
circle(screen, (0, 0, 0), (250, 185), 15)
circle(screen, (0, 0, 0), (150, 185), 10)
rect(screen, (0, 0, 0), (155, 260, 90, 14))
line(screen, (0,0,0), (100,110), (180,165), width =15)
line(screen, (0,0,0), (300,110), (220,155), width =17)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()