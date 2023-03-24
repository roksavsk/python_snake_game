def message(dis, font_style, msg, color):
    msg = font_style.render(msg, True, color)
    dis.blit(msg, [30, 30])


def has_intersects(w_width, w_height, x, y, snake_width, snake_height) -> bool:
    if y <= 0:
        return True
    elif y >= w_height - snake_height:
        return True
    elif x <= 0:
        return True
    elif x >= w_width - snake_width:
        return True
    return False
