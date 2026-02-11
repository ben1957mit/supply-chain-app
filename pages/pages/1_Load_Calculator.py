import streamlit as st
from utils.trailer_data import TRAILERS
from utils.pallet_math import total_volume

st.title("Load Calculator")

num = st.number_input("Number of Pallets", min_value=0)
l = st.number_input("Pallet Length (in)", value=48)
w = st.number_input("Pallet Width (in)", value=40)
h = st.number_input("Pallet Height (in)", value=60)

freight_volume = total_volume(num, l, w, h)
st.write(f"Total Freight Volume: {freight_volume:.2f} cu ft")

results = []
for name, t in TRAILERS.items():
    trailer_vol = t["length"] * t["width"] * t["height"]
    pct = (freight_volume / trailer_vol) * 100
    results.append((name, trailer_vol, pct))

st.subheader("Trailer Comparison")
for r in results:
    st.write(f"{r[0]} — {r[2]:.2f}% full")

best = min([r for r in results if r[2] <= 100], key=lambda x: x[2], default=None)

if best:
    st.success(f"Best Trailer: {best[0]}")
else:
    st.error("Freight does not fit in any trailer.")
