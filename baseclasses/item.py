from baseclasses import Entity


class Item:
    def __repr__(self):
        return "<%s weight=%d>" % (self.name, self.weight)


class GroundItem(Entity):
    def __init__(self, item: Item, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item = item

    def __str__(self):
        return self.item.ground_icon

    def __repr__(self):
        return "<GroundItem item=%s>" % (repr(self.item))
