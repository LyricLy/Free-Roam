from typing import Mapping, Tuple, List

from baseclasses import Entity
from constants import WALK_SPEED, CHUNK_SIZE
from utils import dist
from baseclasses.entity import intersects
from baseclasses.map import generate_map


class Ray:
    def __init__(self, grid: Mapping[Tuple[int, int], List[Entity]], x: int, y: int, dx: int = 0, dy: int = 0):
        self.grid = grid
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def point_to(self, x: int, y: int):
        self.dx, self.dy = generate_map(x, y, self.x, self.y)

    def step(self):
        self.x += self.dx
        self.y += self.dy
        return intersects(self.x, self.y, self.grid[(int(self.x) // CHUNK_SIZE, int(self.y) // CHUNK_SIZE)])

    def step_until_hit(self):
        intersecting = None
        while not intersecting:
            intersecting = self.step()
        return intersecting[0]

    def step_to(self, e: Entity):
        self.point_to(e.x, e.y)
        for _ in range(1 / WALK_SPEED):
            yield from filter(lambda x: x != e, self.step())
