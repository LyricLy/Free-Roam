from baseclasses.entity import Entity, intersects
from utils import plot_direction


class Actor(Entity):
    def __init__(self, *args):
        super().__init__(*args)
        self.go_to_point(*eval(input()))

    def __str__(self):
        return "a"

    def go_to_point(self, x, y):
        self.dx, self.dy = plot_direction(self.x, self.y, x, y)
        self.go_to_x = x
        self.go_to_y = y

    @property
    def size(self):
        return 0.25

    @property
    def volume(self):
        return 0.5

    def step(self):
        if list(intersects(self.go_to_x, self.go_to_y, [self])):
             self.go_to_point(*eval(input()))
        self.move(self.dx, self.dy)
