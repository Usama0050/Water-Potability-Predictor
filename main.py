import pickle
import joblib
import streamlit as st
import numpy as np

with open('model_rfc.pkl', 'rb') as file:
    model = joblib.load('model_rfc.pkl')
    
# Streamlit app
st.title("Water Potability Predictor")
st.markdown("Enter the water quality parameters below:")

# Input fields for user
col1, col2, col3 = st.columns(3)
with col1:
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
    hardness = st.number_input("Hardness (mg/L)", min_value=0.0, max_value=324.0, step=0.1)
    solids = st.number_input("Solids (ppm)", min_value=0.0, max_value=61228.0, step=0.1)
with col2:
    chloramines = st.number_input("Chloramines (ppm)", min_value=0.0, max_value=14.0, step=0.1)
    sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, max_value=482.0, step=0.1)
    conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0, max_value=754.0, step=0.1)
with col3:
    organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0, max_value=29.0, step=0.1)
    trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, max_value=124.0, step=0.1)
    turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, max_value=7.0, step=0.1)

# Prediction
if st.button("Predict Potability"):
    features = np.array([[ph, hardness, solids, chloramines, sulfate,
                          conductivity, organic_carbon, trihalomethanes, turbidity]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("✅ The water is **potable** (safe to drink).")
    else:
        st.error("❌ The water is **not potable** (not safe to drink).")
