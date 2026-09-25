# Project Report

## Title

AI-Based Warehouse Picking Path Optimizer

## Objective

Build a prototype that helps warehouse pickers reduce unnecessary walking by generating efficient routes through a warehouse grid.

## Problem Statement

Order picking is a major source of warehouse effort. Route quality affects walking time, throughput, workload balance and service performance.

## Proposed System

The system receives warehouse layout and order information. It identifies item locations, generates paths using A*, and creates an optimized multi-item picking route.

## Workflow

1. Observe orders and warehouse layout.
2. Identify item locations.
3. Assign orders to available pickers.
4. Generate paths using A*.
5. Build the multi-item route.
6. Compare with a baseline route.
7. Display distance and estimated walking time.
8. Use the result as the recommendation for the next picking wave.

## Algorithm

A* combines actual path cost with a heuristic estimate:

`f(n) = g(n) + h(n)`

For the four-direction warehouse grid, Manhattan distance is used as the heuristic.

## Metrics

- Travel distance
- Estimated walking time
- Distance saved
- Picker workload
- Number of orders assigned

## Pilot Approach

A practical rollout can begin with a baseline period, then one representative zone, followed by shadow-mode testing and review before expansion.

## Future Work

- Live order arrival
- Congestion-aware routing
- Dynamic re-routing
- Real WMS integration
- Historical learning
- Supervisor override
- Multi-picker collision avoidance
