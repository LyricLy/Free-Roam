from abc import ABC, abstractmethod
from typing import List

from constants import CHUNK_SIZE
from utils import bind, dist


class Entity(ABC):
    def __init__(self, map, x: int, y: int):
        self.map = map
        self.x = x
        self.y = y

    def move(self, dx: int, dy: int):
        new_x, new_y = bind(self.x + dx, self.map.max_x), bind(self.y + dy, self.map.max_y)

        self.map.entity_grid[(self.x // CHUNK_SIZE, self.y // CHUNK_SIZE)].remove(self)
        self.map.entity_grid[(new_x // CHUNK_SIZE, new_y // CHUNK_SIZE)].append(self)

        self.x = new_x
        self.y = new_y
        return new_x, new_y

    def step(self):
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def volume(self) -> int:
        pass


def intersects(x: int, y: int, entities: List[Entity]):
    return (e for e in entities if dist(x, y, e.x, e.y) <= e.size)
