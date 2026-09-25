class Picker:
    def __init__(self, picker_id, capacity):
        self.picker_id = picker_id
        self.capacity = capacity
        self.orders = []

    @property
    def workload(self):
        return len(self.orders)
