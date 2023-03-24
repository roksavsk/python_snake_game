from time import sleep

import pygame
from helpers import message, has_intersects

# CONSTANTS
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

SNAKE_WIDTH = 10
SNAKE_HEIGHT = 10

VELOCITY = 5

# VARIABLES
X = 200
Y = 150

X_APPEND = 0
Y_APPEND = 0

# Start
pygame.init()
dis = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.update()
pygame.display.set_caption('Snake game!')

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

# Start screen
# dis.fill(BLUE)
# pygame.display.flip()
# sleep(1)
# dis.fill(GREEN)
# pygame.display.flip()
# sleep(1)

game_run = True
while game_run:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                X_APPEND = -VELOCITY
                Y_APPEND = 0
            elif event.key == pygame.K_RIGHT:
                X_APPEND = VELOCITY
                Y_APPEND = 0
            elif event.key == pygame.K_UP:
                X_APPEND = 0
                Y_APPEND = -VELOCITY
            elif event.key == pygame.K_DOWN:
                X_APPEND = 0
                Y_APPEND = VELOCITY

    if has_intersects(WINDOW_WIDTH, WINDOW_HEIGHT, X, Y, SNAKE_WIDTH, SNAKE_HEIGHT):
        game_run = False

    X += X_APPEND
    Y += Y_APPEND

    dis.fill(WHITE)
    pygame.draw.rect(dis, BLUE, [X, Y, SNAKE_WIDTH, SNAKE_HEIGHT])
    pygame.display.update()
    clock.tick(10)

message(dis, font_style, "Game Over", RED)
pygame.display.update()
sleep(1)

pygame.quit()
quit()
