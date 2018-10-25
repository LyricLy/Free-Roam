from baseclasses.map import Map


def do(map: Map):
    print(map)
    for e in map.entities:
        e.step()
