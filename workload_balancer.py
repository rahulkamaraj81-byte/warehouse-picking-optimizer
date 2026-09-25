from models.picker import Picker

def assign_orders(orders, picker_configs):
    """Simple capacity-aware round-robin assignment."""
    pickers = [
        Picker(p["picker_id"], p["capacity"])
        for p in picker_configs
    ]

    for order in orders:
        available = [p for p in pickers if p.workload < p.capacity]
        if not available:
            raise ValueError("Not enough picker capacity for all orders.")
        picker = min(available, key=lambda p: p.workload)
        picker.orders.append(order)

    return pickers
