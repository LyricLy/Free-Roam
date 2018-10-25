from baseclasses.entity import Entity


class Rock(Entity):
    @property
    def size(self):
        return 0.5

    @property
    def volume(self):
        return 0.25

    def __str__(self):
        return "b"


class Tree(Entity):
    @property
    def size(self):
        return 0.4

    @property
    def volume(self):
        return 0.6

    def __str__(self):
        return "t"
