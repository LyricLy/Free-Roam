from abc import ABC, abstractmethod


class Biome(ABC):
    """A world biome.
    Biomes work on a Voronoi diagram; Biome objects represent a point on the diagram.
    For each location, the nearest biome point is that location's biome.

    Arguments:
    x -- The x coordinate of the biome point.
    y -- The y coordinate of the biome point.

    Abstract methods:
    get_entity -- Given a point, return an Entity at that point that appears in this biome.
    """

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @abstractmethod
    def get_entity(self, map, x: int, y: int):
        """Return an Entity from this biome."""
