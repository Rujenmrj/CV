import pygame
import sys
from pygame.math import Vector2
import random


class snake:
    def __init__(self):
        self.x = 5
        self.y = 2
        self.pos = Vector2(snake.x, snake.y)

pygame.init()
WIDTH, HEIGHT = 30, 20
Window = pygame.display.set_mode((WIDTH*HEIGHT, WIDTH*HEIGHT))
clock = pygame.time.Clock()

while True:

    Window.fill((0, 75, 25))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
