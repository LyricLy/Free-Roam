import time

from biomes import BIOMES
from constants import WORLD_SIZE, TICK_RATE, BIOME_WEIGHTS, BIOME_VARIATION, OBJECT_DENSITY, ACTORS
from step import do
from baseclasses.map import generate_map


start = time.time()
map = generate_map(WORLD_SIZE, WORLD_SIZE, BIOMES, BIOME_WEIGHTS, BIOME_VARIATION, OBJECT_DENSITY, ACTORS)

while True:
    do(map)
    time.sleep(TICK_RATE - ((time.time() - start) % TICK_RATE))
