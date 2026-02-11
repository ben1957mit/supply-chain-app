import streamlit as st
from utils.layout_engine import generate_layout
from utils.trailer_data import TRAILERS
from utils.pallet_math import pallets_per_row, rows_per_trailer

st.title("Trailer Layout Visualizer")

trailer = st.selectbox("Trailer Type", list(TRAILERS.keys()))
pallet_w = st.number_input("Pallet Width (in)", value=40)
pallet_l = st.number_input("Pallet Length (in)", value=48)

t = TRAILERS[trailer]

cols = pallets_per_row(t["width"], pallet_w)
rows = rows_per_trailer(t["length"], pallet_l)

layout = generate_layout(rows, cols)

st.subheader("Top‑Down Pallet Layout")

for row in layout:
    st.text(" ".join(row))
