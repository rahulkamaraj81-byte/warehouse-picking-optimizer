# AI-Based Warehouse Picking Path Optimizer

An educational warehouse optimization project that finds efficient picker routes using the A* pathfinding algorithm and provides a simple Streamlit dashboard.

## Problem

Warehouse pickers may travel through many aisles to collect items for an order. Extra walking increases effort and can affect throughput and service. This project models the warehouse as a grid, finds routes between item locations, and compares the optimized route with a simple baseline.

The project follows the source concept of:
**Observe → Learn → Recommend → Adapt**

## Features

- Warehouse grid with blocked cells
- Multiple customer orders
- Item-to-location mapping
- A* pathfinding
- Multi-item picking route
- Distance and estimated walking time
- Simple picker assignment
- Workload summary
- Interactive Streamlit visualization
- Baseline vs optimized route comparison

## Project Structure

```text
warehouse-picking-optimizer/
├── README.md
├── requirements.txt
├── main.py
├── data/
│   ├── warehouse.json
│   ├── orders.json
│   └── pickers.json
├── algorithms/
│   ├── astar.py
│   ├── route_optimizer.py
│   └── workload_balancer.py
├── models/
│   ├── warehouse.py
│   ├── order.py
│   └── picker.py
├── visualization/
│   └── warehouse_map.py
├── dashboard/
│   └── app.py
├── tests/
│   └── test_astar.py
└── docs/
    └── project_report.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the command-line demo

```bash
python main.py
```

## Run the dashboard

```bash
streamlit run dashboard/app.py
```

## Algorithm

The warehouse is represented as a grid. Each walkable cell is a node and adjacent cells are connected.

A* uses:

**f(n) = g(n) + h(n)**

where:

- `g(n)` = cost from the start to the current cell
- `h(n)` = estimated cost from the current cell to the goal
- `f(n)` = total estimated cost

The default heuristic is Manhattan distance.

## Metrics

The demo reports:

- Baseline route distance
- Optimized route distance
- Distance saved
- Estimated walking time
- Number of item locations
- Picker workload

## Limitations

This is a prototype for academic demonstration. It does not connect to a real WMS, live scanner stream, or production warehouse.

## Future Enhancements

- Live order arrival
- Real congestion data
- Real WMS integration
- Multiple picker collision avoidance
- Machine-learning demand prediction
- Historical route learning
- Supervisor override interface
