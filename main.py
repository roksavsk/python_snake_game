import random
from time import sleep

import pygame
from helpers import message, has_intersects_borders, generate_food, snake_intersects_block, \
    snake_intersects_itself, generate_wall, snake_intersects_brick, generate_bricks

# CONSTANTS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 500

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
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
grey35 = pygame.Color('grey35')

SNAKE_WIDTH, SNAKE_HEIGHT = 10, 10
FOOD_WIDTH, FOOD_HEIGHT = SNAKE_WIDTH, SNAKE_HEIGHT
BRICK_SIZE = 10

VELOCITY = 10

# VARIABLES
SNAKE = []
WALL = generate_wall(WINDOW_WIDTH, WINDOW_HEIGHT, BRICK_SIZE)
BRICKS = generate_bricks(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)

X = 200
Y = 150

X_APPEND = 0
Y_APPEND = 0

FOOD_X = 0
FOOD_Y = 0

SCORE = 0


def direction_x_by_append(x_append):
    return True if x_append else False


# Start
pygame.init()
dis = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.update()
pygame.display.set_caption('Snake game!')

clock = pygame.time.Clock()
font_style_start = pygame.font.SysFont('Arial Black', 50)
font_style = pygame.font.SysFont('Arial Black', 30)
font_style_score = pygame.font.SysFont('Tahoma', 25)
game_run = True
game_end = False
game_before_init = True
new_head = False

# Start screen animation
dis.fill(royalblue)
pygame.display.flip()
sleep(0.4)
dis.fill(limegreen)
pygame.display.flip()
sleep(0.4)
dis.fill(YELLOW)
message(dis, font_style_start, "Let's go!", royalblue4, 275, 200)
pygame.display.update()
pygame.display.flip()
sleep(1)

while game_run:
    dis.fill(springgreen3)
    message(dis, font_style_score, f"Score: {SCORE}", indigo, 30, 30)

    while game_end:
        message(dis, font_style, "Game Over. Press C to continue or Q to exit", YELLOW, 30, 200)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
                game_end = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    game_end = False
                    game_run = True
                    X = 200
                    Y = 150
                    X_APPEND = 0
                    Y_APPEND = 0
                    SNAKE = [[X, Y]]
                    SCORE = 0

                if event.key == pygame.K_q:
                    game_end = False
                    game_run = False

    for event in pygame.event.get():

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

    if snake_intersects_block(
            X, Y,
            SNAKE_WIDTH, SNAKE_HEIGHT,
            direction_x_by_append(X_APPEND),
            FOOD_X, FOOD_Y,
            FOOD_WIDTH, FOOD_HEIGHT
    ):
        FOOD_X, FOOD_Y = generate_food(WINDOW_WIDTH, WINDOW_HEIGHT, SNAKE_WIDTH, SNAKE_HEIGHT)
        new_head = True
        SCORE += 1

    X += X_APPEND
    Y += Y_APPEND

    snake_head = [X, Y]
    SNAKE.append(snake_head)

    if len(SNAKE) > 1:
        del SNAKE[0]

    if new_head:
        X += X_APPEND
        Y += Y_APPEND
        SNAKE.append([X, Y])
        new_head = False

    if snake_intersects_itself(SNAKE):
        game_end = True

    # Draw
    if FOOD_X is not None and FOOD_Y is not None:
        pygame.draw.rect(dis, magenta3, [FOOD_X, FOOD_Y, FOOD_WIDTH, FOOD_HEIGHT])

    for coord_block in SNAKE:
        pygame.draw.rect(dis, royalblue4, [coord_block[0], coord_block[1], SNAKE_WIDTH, SNAKE_HEIGHT])

    if SCORE > 5:
        for brick in WALL:
            pygame.draw.rect(dis, grey35, [brick[0], brick[1], BRICK_SIZE, BRICK_SIZE])

        if snake_intersects_brick(SNAKE[-1], WALL):
            game_end = True

    if SCORE > 10:
        for brick in BRICKS:
            pygame.draw.rect(dis, grey35, [brick[0], brick[1], BRICK_SIZE, BRICK_SIZE])

        if snake_intersects_brick(SNAKE[-1], BRICKS):
            game_end = True

    pygame.display.update()
    clock.tick(10)

pygame.quit()
quit()
