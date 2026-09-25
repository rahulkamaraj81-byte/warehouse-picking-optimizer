class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def locations(self, warehouse):
        return [warehouse.location_for(item) for item in self.items]
