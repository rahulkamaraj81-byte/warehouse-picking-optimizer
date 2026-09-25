from models.warehouse import Warehouse
from algorithms.astar import astar

def test_astar_finds_path():
    warehouse = Warehouse(
        width=5,
        height=5,
        blocked=[],
        start=[0, 0],
        item_locations={}
    )
    path = astar(warehouse, (0, 0), (4, 4))
    assert path[0] == (0, 0)
    assert path[-1] == (4, 4)
    assert len(path) == 9

def test_astar_avoids_blocked_cell():
    warehouse = Warehouse(
        width=5,
        height=5,
        blocked=[[1, 0]],
        start=[0, 0],
        item_locations={}
    )
    path = astar(warehouse, (0, 0), (2, 0))
    assert (1, 0) not in path
