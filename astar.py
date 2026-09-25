import heapq

DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

def heuristic(a, b):
    """Manhattan-distance heuristic for a 4-direction grid."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    """Return the shortest walkable path from start to goal."""
    if start == goal:
        return [start]

    open_heap = []
    heapq.heappush(open_heap, (heuristic(start, goal), 0, start))
    came_from = {}
    g_score = {start: 0}
    visited = set()

    while open_heap:
        _, current_cost, current = heapq.heappop(open_heap)

        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for dx, dy in DIRECTIONS:
            neighbor = (current[0] + dx, current[1] + dy)

            if not grid.is_walkable(neighbor):
                continue

            new_cost = current_cost + 1
            if new_cost < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = new_cost
                f_score = new_cost + heuristic(neighbor, goal)
                heapq.heappush(open_heap, (f_score, new_cost, neighbor))

    return None
