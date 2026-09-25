import json
import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from models.warehouse import Warehouse
from models.order import Order
from algorithms.route_optimizer import (
    route_for_order, baseline_route, path_distance, estimated_minutes
)
from algorithms.workload_balancer import assign_orders
from visualization.warehouse_map import plot_route

st.set_page_config(page_title="Warehouse Route Optimizer", layout="wide")
st.title("AI-Based Warehouse Picking Path Optimizer")
st.caption("A* route optimization + simple picker workload balancing")

with open(ROOT / "data/warehouse.json") as f:
    warehouse = Warehouse(**json.load(f))
with open(ROOT / "data/orders.json") as f:
    orders = [Order(**o) for o in json.load(f)]
with open(ROOT / "data/pickers.json") as f:
    picker_data = json.load(f)

order_names = [o.order_id for o in orders]
selected_name = st.sidebar.selectbox("Select order", order_names)
order = next(o for o in orders if o.order_id == selected_name)

optimized = route_for_order(warehouse, order)
baseline = baseline_route(warehouse, order)

baseline_distance = path_distance(baseline)
optimized_distance = path_distance(optimized)
saving = baseline_distance - optimized_distance

c1, c2, c3, c4 = st.columns(4)
c1.metric("Baseline", f"{baseline_distance} cells")
c2.metric("Optimized", f"{optimized_distance} cells")
c3.metric("Saved", f"{saving} cells")
c4.metric("Walking time", f"{estimated_minutes(optimized):.1f} min")

st.subheader("Optimized Route")
fig = plot_route(warehouse, optimized, f"{order.order_id} - Optimized Route")
st.pyplot(fig)

st.subheader("Route Details")
st.write("Items:", ", ".join(order.items))
st.write("Path:", " → ".join(f"({x},{y})" for x, y in optimized))

st.subheader("Picker Workload")
pickers = assign_orders(orders, picker_data)
for picker in pickers:
    st.write(
        f"**{picker.picker_id}** — "
        f"{picker.workload}/{picker.capacity} orders — "
        f"{', '.join(o.order_id for o in picker.orders) or 'No orders'}"
    )

st.info(
    "Prototype note: this demo uses static sample data. "
    "A production system would connect to WMS orders, live scans, "
    "congestion and supervisor feedback."
)
