import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json

# Load the trained pipeline and feature names
model = joblib.load("models/final_model.pkl")

with open("models/feature_names.json") as f:
    expected_features = json.load(f)

st.title("❤️ Heart Disease Prediction App")

st.markdown("### Enter Patient Data")

# Create input fields
age = st.number_input("Age", min_value=1, max_value=120, value=50)
sex_label = st.selectbox("Sex", options=["Female", "Male"])
sex = 1 if sex_label == "Male" else 0
cp_2 = st.selectbox("Chest Pain Type: cp_2.0", options=[0, 1])
cp_3 = st.selectbox("Chest Pain Type: cp_3.0", options=[0, 1])
cp_4 = st.selectbox("Chest Pain Type: cp_4.0", options=[0, 1])
trestbps = st.number_input("Resting Blood Pressure", min_value=0, value=120)
chol = st.number_input("Cholesterol", min_value=0, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1])
restecg_2 = st.selectbox("Resting ECG: restecg_2.0", options=[0, 1])
thalach = st.number_input("Max Heart Rate Achieved", min_value=0, value=150)
exang = st.selectbox("Exercise Induced Angina", options=[0, 1])
oldpeak = st.number_input("ST depression", min_value=0.0, value=1.0)
slope_2 = st.selectbox("Slope: slope_2.0", options=[0, 1])
ca = st.selectbox("Number of Major Vessels (0–3)", options=[0, 1, 2, 3])
thal_7 = st.selectbox("Thal: thal_7.0", options=[0, 1])

# Create DataFrame for input
input_data = {
    'age': age,
    'sex': sex,
    'cp_2.0': cp_2,
    'cp_3.0': cp_3,
    'cp_4.0': cp_4,
    'trestbps': trestbps,
    'chol': chol,
    'fbs': fbs,
    'restecg_2.0': restecg_2,
    'thalach': thalach,
    'exang': exang,
    'oldpeak': oldpeak,
    'slope_2.0': slope_2,
    'ca': ca,
    'thal_7.0': thal_7,
}
input_df = pd.DataFrame([input_data])

# Ensure all features are present and in correct order
for col in expected_features:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[expected_features]

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.subheader("🩺 Prediction Result:")
    st.write("Positive for Heart Disease" if prediction == 1 else "Negative for Heart Disease")
    st.write(f"🔢 Probability: {prob:.2%}")
