import json
from models.warehouse import Warehouse
from models.order import Order
from algorithms.route_optimizer import (
    route_for_order, baseline_route, path_distance, estimated_minutes
)
from algorithms.workload_balancer import assign_orders

def load_data():
    with open("data/warehouse.json") as f:
        warehouse_data = json.load(f)
    with open("data/orders.json") as f:
        order_data = json.load(f)
    with open("data/pickers.json") as f:
        picker_data = json.load(f)

    warehouse = Warehouse(**warehouse_data)
    orders = [Order(**o) for o in order_data]
    return warehouse, orders, picker_data

def main():
    warehouse, orders, picker_data = load_data()

    print("\nAI-Based Warehouse Picking Path Optimizer")
    print("=" * 45)

    for order in orders:
        baseline = baseline_route(warehouse, order)
        optimized = route_for_order(warehouse, order)

        b = path_distance(baseline)
        o = path_distance(optimized)
        saving = b - o

        print(f"\n{order.order_id}: {order.items}")
        print(f"Baseline distance : {b} cells")
        print(f"Optimized distance: {o} cells")
        print(f"Distance saved    : {saving} cells")
        print(f"Estimated time    : {estimated_minutes(optimized):.1f} min")

    pickers = assign_orders(orders, picker_data)
    print("\nPicker Assignment")
    for picker in pickers:
        print(picker.picker_id, "->", [o.order_id for o in picker.orders])

if __name__ == "__main__":
    main()
