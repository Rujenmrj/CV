import pygame
import sys
from pygame.math import Vector2
import random


class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(0, 1)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(
                int(block.x*CELLSIZE), int(block.y*CELLSIZE), CELLSIZE, CELLSIZE)
            pygame.draw.rect(Window, (0, 100, 100), snake_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0]+self.direction)
        self.body = body_copy[:]

    def add_body(self):
        self.new_block = True


class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            int(self.pos.x*CELLSIZE), int(self.pos.y*CELLSIZE), CELLSIZE, CELLSIZE)
        pygame.draw.rect(Window, (226, 0, 0), fruit_rect)

    def randomize(self):
        self.x = random.randint(0, CELL_NUM-1)
        self.y = random.randint(0, CELL_NUM-1)
        self.pos = Vector2(self.x, self.y)


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collission()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collission(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_body()


pygame.init()
CELLSIZE, CELL_NUM = 30, 20
Window = pygame.display.set_mode((CELLSIZE*CELL_NUM, CELLSIZE*CELL_NUM))
clock = pygame.time.Clock()

main_game = Main()

Window_update = pygame.USEREVENT
pygame.time.set_timer(Window_update, 200)

while True:

    Window.fill((0, 75, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if event.type == Window_update:
        main_game.update()

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        main_game.snake.direction = Vector2(-1, 0)
    if key[pygame.K_d] == True:
        main_game.snake.direction = Vector2(1, 0)
    elif key[pygame.K_w] == True:
        main_game.snake.direction = Vector2(0, -1)
    elif key[pygame.K_s] == True:
        main_game.snake.direction = Vector2(0, 1)

    Window.fill((175, 215, 70))
    main_game.draw_elements()

    pygame.display.update()
    clock.tick(10)
