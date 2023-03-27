import random
from time import sleep

import pygame
from helpers import message, has_intersects_borders, generate_food, has_intersects_food

# CONSTANTS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = pygame.Color('yellow')
FIREBRICK = pygame.Color('firebrick')
darkslateblue = pygame.Color('darkslateblue')
mediumseagreen = pygame.Color('mediumseagreen')
springgreen3 = pygame.Color('springgreen3')
royalblue4 = pygame.Color('royalblue4')
royalblue = pygame.Color('royalblue')
limegreen = pygame.Color('limegreen')
orangered4 = pygame.Color('orangered4')
indigo = pygame.Color('indigo')
magenta3 = pygame.Color('magenta3')

SNAKE_WIDTH, SNAKE_HEIGHT = 10, 10
FOOD_WIDTH, FOOD_HEIGHT = SNAKE_WIDTH, SNAKE_HEIGHT


VELOCITY = 10

# VARIABLES
SNAKE = []
X = 200
Y = 150

X_APPEND = 0
Y_APPEND = 0

FOOD_X = 0
FOOD_Y = 0

# Start
pygame.init()
dis = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.update()
pygame.display.set_caption('Snake game!')

clock = pygame.time.Clock()
font_style = pygame.font.SysFont('Tahoma', 30)
game_run = True
game_end = False
game_before_init = True

# Start screen animation
dis.fill(royalblue)
pygame.display.flip()
sleep(0.6)
dis.fill(limegreen)
pygame.display.flip()
sleep(0.6)
dis.fill(YELLOW)
pygame.display.flip()
sleep(0.6)

while game_run:

    while game_end:
        message(dis, font_style, "Game Over. Press C to continue or Q to exit", indigo)
        pygame.display.update()

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_end = False
                    game_run = True
                    X = 200
                    Y = 150
                    X_APPEND = 0
                    Y_APPEND = 0

                if event.key == pygame.K_q:
                    game_end = False
                    game_run = False
                    break

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            game_run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_APPEND = -VELOCITY
                Y_APPEND = 0
                if game_before_init:
                    FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)
                    game_before_init = False

            elif event.key == pygame.K_RIGHT:
                X_APPEND = VELOCITY
                Y_APPEND = 0
                if game_before_init:
                    FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)
                    game_before_init = False

            elif event.key == pygame.K_UP:
                X_APPEND = 0
                Y_APPEND = -VELOCITY
                if game_before_init:
                    FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)
                    game_before_init = False

            elif event.key == pygame.K_DOWN:
                X_APPEND = 0
                Y_APPEND = VELOCITY
                if game_before_init:
                    FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)
                    game_before_init = False

    if has_intersects_borders(WINDOW_WIDTH, WINDOW_HEIGHT, X, Y, SNAKE_WIDTH, SNAKE_HEIGHT):
        game_end = True

    if has_intersects_food(X, Y, X_APPEND, Y_APPEND, SNAKE_WIDTH, SNAKE_HEIGHT, FOOD_X, FOOD_Y, FOOD_WIDTH, FOOD_HEIGHT):
        FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)

    X += X_APPEND
    Y += Y_APPEND

    snake_head = [X, Y]
    SNAKE.append(snake_head)

    if len(SNAKE) > 1:
        del SNAKE[0]

    # Draw
    dis.fill(springgreen3)
    pygame.draw.rect(dis, royalblue4, [X, Y, SNAKE_WIDTH, SNAKE_HEIGHT])

    if FOOD_X is not None and FOOD_Y is not None:
        pygame.draw.rect(dis, magenta3, [FOOD_X, FOOD_Y, FOOD_WIDTH, FOOD_HEIGHT])

    pygame.display.update()
    clock.tick(10)

pygame.quit()
quit()
