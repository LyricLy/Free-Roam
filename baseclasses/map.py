from collections import defaultdict
from random import choices, randint
from typing import List, Tuple, Mapping

from actor import Actor
from baseclasses.biome import Biome
from baseclasses.entity import Entity, intersects
from constants import CHUNK_SIZE
from utils import dist


class Map:
    def __init__(self, max_x: int, max_y: int,
                 biomes: List[Biome], entity_points: List[Tuple[int, int]], actor_points: List[Entity] = None):
        actor_points = actor_points or []
        self.biomes = biomes
        self.max_x = max_x
        self.max_y = max_y

        self.entities: List[Entity] = ([x for x in (self.biome(*p).get_entity(self, *p) for p in entity_points) if x]
                                       + [Actor(self, *p) for p in actor_points])
        self.entity_grid: Mapping[Tuple[int, int], List[Entity]] = defaultdict(list)

        for e in self.entities:
            rounded_point: Tuple[int, int] = tuple([int(x) // CHUNK_SIZE for x in (e.x, e.y)])
            self.entity_grid[rounded_point].append(e)

    def __str__(self):
        matrix = [[str(self.biome(x, y)) for x in range(self.max_x + 1)] for y in range(self.max_y + 1)]
        for e in self.entities:
            matrix[int(e.y)][int(e.x)] = str(e)
        return "\n".join([" ".join(y) for y in matrix])

    def biome(self, x: int, y: int):
        return min(self.biomes, key=lambda b: dist(x, y, b.x, b.y))

    def intersects(self, x: int, y: int):
        return intersects(x, y, self.entities)


def generate_map(x: int, y: int,
                 biomes: List[Biome], biome_weights: List[int], biome_variation: int,
                 object_density: int, actors: int = 0):
    return Map(x, y,
               [choices(biomes, biome_weights)[0](randint(0, x), randint(0, y)) for _ in range(biome_variation)],
               [(randint(0, x), randint(0, y)) for _ in range(object_density)],
               [(randint(0, x), randint(0, y)) for _ in range(actors)])
