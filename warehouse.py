class Warehouse:
    def __init__(self, width, height, blocked, start, item_locations):
        self.width = width
        self.height = height
        self.blocked = {tuple(p) for p in blocked}
        self.start = tuple(start)
        self.item_locations = {
            item: tuple(pos) for item, pos in item_locations.items()
        }

    def is_walkable(self, pos):
        x, y = pos
        return (
            0 <= x < self.width
            and 0 <= y < self.height
            and pos not in self.blocked
        )

    def location_for(self, item):
        return self.item_locations[item]
