import matplotlib.pyplot as plt

def plot_route(warehouse, path=None, title="Warehouse Picking Route", ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    blocked_x = [p[0] for p in warehouse.blocked]
    blocked_y = [p[1] for p in warehouse.blocked]
    ax.scatter(blocked_x, blocked_y, marker="s", s=250, label="Blocked")

    if path:
        xs = [p[0] for p in path]
        ys = [p[1] for p in path]
        ax.plot(xs, ys, marker="o", linewidth=2, label="Route")

    sx, sy = warehouse.start
    ax.scatter([sx], [sy], s=120, marker="*", label="Start")

    for item, pos in warehouse.item_locations.items():
        ax.scatter([pos[0]], [pos[1]], s=90)
        ax.text(pos[0] + 0.12, pos[1] + 0.12, item)

    ax.set_xlim(-1, warehouse.width)
    ax.set_ylim(-1, warehouse.height)
    ax.set_aspect("equal")
    ax.set_xticks(range(warehouse.width))
    ax.set_yticks(range(warehouse.height))
    ax.grid(True, alpha=0.3)
    ax.set_title(title)
    ax.legend()
    return ax
