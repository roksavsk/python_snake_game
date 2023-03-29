import random


def message(dis, font_style, msg, color, x, y):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [x, y])


def has_intersects_borders(w_width, w_height, x, y, snake_width, snake_height) -> bool:
    if y <= 0:
        return True
    elif y >= w_height - snake_height:
        return True
    elif x <= 0:
        return True
    elif x >= w_width - snake_width:
        return True
    return False


def has_intersects_food(snake_x, snake_y,
                        snake_x_append, snake_y_append,
                        snake_width, snake_height,
                        food_x, food_y,
                        food_width, food_height) -> bool:
    if food_x is None or food_y is None:
        return False

    if (snake_x + snake_width == food_x) and (snake_y == food_y) and snake_x_append:
        return True  # left side
    if (snake_x == food_x) and (snake_y + snake_height == food_y) and snake_y_append:
        return True  # top side
    if (snake_x == food_x + food_width) and (snake_y == food_y) and snake_x_append:
        return True  # right side
    if (snake_x == food_x) and (snake_y == food_y + food_height) and snake_y_append:
        return True  # bottom side

    return False


def snake_intersects_block(snake_x, snake_y,
                           snake_width, snake_height,
                           direction_x,
                           block_x, block_y,
                           block_width, block_height) -> bool:
    """

    :param snake_x:
    :param snake_y:
    :param snake_width:
    :param snake_height:
    :param direction_x: True if direction on Y axis, False - Y
    :param block_x:
    :param block_y:
    :param block_width:
    :param block_height:
    :return:
    """

    # if check_direction:
    #     direction_y = not direction_x
    #     direction_x = direction_x
    # else:
    #     direction_y = True
    #     direction_x = True
    direction_y = not direction_x

    if block_x is None or block_y is None:
        return False

    if (snake_x + snake_width == block_x) and (snake_y == block_y) and direction_x:
        return True  # left side
    if (snake_x == block_x) and (snake_y + snake_height == block_y) and direction_y:
        return True  # top side
    if (snake_x == block_x + block_width) and (snake_y == block_y) and direction_x:
        return True  # right side
    if (snake_x == block_x) and (snake_y == block_y + block_height) and direction_y:
        return True  # bottom side

    return False


def snake_intersects_itself(snake):
    for block in snake[:-1]:
        if block == snake[-1]:
            return True


def snake_intersects_brick(snake_head, bricks):
    for block in bricks:
        if block == snake_head:
            return True


def to_ten(n):
    return round(n / 10.0) * 10.0


def generate_food(w_width, w_height, snake_width, snake_height):
    return (
        to_ten(random.randrange(0, w_width - snake_width)),
        to_ten(random.randrange(0, w_height - snake_height))
    )


def generate_wall(w_width, w_height, brick_size) -> list:
    bricks_x = int(to_ten(w_width / 2))
    brick_y_start = int(to_ten(w_height / 4))
    brick_y_end = int(to_ten(w_height - w_height / 4))
    return [[bricks_x, y] for y in range(brick_y_start, brick_y_end, brick_size)]


def generate_bricks(w_width, w_height, snake_width, snake_height):
    return [[to_ten(random.randrange(0, w_width - snake_width)), to_ten(random.randrange(0, w_height - snake_height))]
            for x in range(10)]
