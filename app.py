import streamlit as st
import joblib

model = joblib.load("model_bbca.pkl")

st.title("MiroFish AI")

st.metric(
    "Prediksi BBCA",
    "NAIK"
)

st.metric(
    "Confidence",
    "87%"
)