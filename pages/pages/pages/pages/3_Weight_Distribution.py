import streamlit as st
from utils.weight_math import axle_split, weight_okay
from utils.trailer_data import TRAILERS

st.title("Weight Distribution")

trailer = st.selectbox("Trailer Type", list(TRAILERS.keys()))
weight = st.number_input("Total Freight Weight (lbs)", min_value=0)

max_w = TRAILERS[trailer]["max_weight"]

steer, drive, tandem = axle_split(weight)

st.write(f"Steer Axle: {steer:.0f} lbs")
st.write(f"Drive Axle: {drive:.0f} lbs")
st.write(f"Tandem Axle: {tandem:.0f} lbs")

if weight_okay(weight, max_w):
    st.success("Weight is within legal limits.")
else:
    st.error("Overweight load.")
