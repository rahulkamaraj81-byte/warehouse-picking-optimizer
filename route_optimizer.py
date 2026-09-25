from algorithms.astar import astar

def route_for_order(warehouse, order):
    """Build a route that visits all requested item locations."""
    current = warehouse.start
    full_path = [current]
    targets = order.locations(warehouse)

    # Greedy nearest-next target selection reduces unnecessary movement
    # while A* finds the shortest path between each pair.
    remaining = set(targets)

    while remaining:
        next_target = min(
            remaining,
            key=lambda p: abs(current[0] - p[0]) + abs(current[1] - p[1])
        )
        segment = astar(warehouse, current, next_target)
        if segment is None:
            raise ValueError(f"No path from {current} to {next_target}")
        full_path.extend(segment[1:])
        current = next_target
        remaining.remove(next_target)

    return full_path

def baseline_route(warehouse, order):
    """Baseline: visit item locations in the order they appear."""
    current = warehouse.start
    full_path = [current]

    for target in order.locations(warehouse):
        segment = astar(warehouse, current, target)
        if segment is None:
            raise ValueError(f"No path from {current} to {target}")
        full_path.extend(segment[1:])
        current = target

    return full_path

def path_distance(path):
    return max(0, len(path) - 1)

def estimated_minutes(path, cells_per_minute=2.0):
    return path_distance(path) / cells_per_minute
