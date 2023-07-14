import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 30, 20
Window = pygame.display.set_mode((WIDTH*HEIGHT, WIDTH*HEIGHT))
clock = pygame.time.Clock()

while True:

    Window.fill((0, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
