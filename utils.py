from constants import WALK_SPEED


def dist(x: int, y: int, other_x: int, other_y: int):
    width, length = abs(x - other_x), abs(y - other_y)
    return ((width ** 2) + (length ** 2)) ** 0.5


def bind(i: int, mx: int):
    return 0 if i < 0 else i if i < mx else mx


def plot_direction(x: int, y: int, other_x: int, other_y: int):
    xd = other_x - x
    yd = other_y - y
    if xd:
        dx = xd / (dist(other_x, other_y, x, y) / WALK_SPEED)
        dy = dx * (yd / xd)
        return dx, dy
    else:
        return 0, yd / WALK_SPEED
