import streamlit as st
from utils.pallet_math import pallets_per_row, rows_per_trailer
from utils.trailer_data import TRAILERS

st.title("Pallet Pattern Optimization")

trailer = st.selectbox("Trailer Type", list(TRAILERS.keys()))
pallet_w = st.number_input("Pallet Width (in)", value=40)
pallet_l = st.number_input("Pallet Length (in)", value=48)

t = TRAILERS[trailer]

cols = pallets_per_row(t["width"], pallet_w)
rows = rows_per_trailer(t["length"], pallet_l)

st.write(f"Max pallets (standard orientation): {cols * rows}")
