from baseclasses.biome import Biome
from baseclasses.map import Map
from obstacles import Tree


class Forest(Biome):
    def get_entity(self, map: Map, x: int, y: int):
        return Tree(map, x, y)

    def __str__(self):
        return ";"


class Ocean(Biome):
    def get_entity(self, map: Map, x: int, y: int):
        return None

    def __str__(self):
        return "w"


BIOMES = [Forest, Ocean]
