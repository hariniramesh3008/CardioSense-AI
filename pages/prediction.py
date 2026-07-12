import streamlit as st
import pandas as pd
import joblib

# ----------------------------
# LOAD MODEL
# ----------------------------
model = joblib.load("models/cardiosense_model.pkl")
scaler = joblib.load("models/scaler.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")
st.title("🩺 Heart Disease Prediction")

# ----------------------------
# INPUTS
# ----------------------------

age = st.number_input("Age", 18, 100, 45)

sex = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

dataset = st.selectbox(
    "Hospital Dataset",
    [
        "Cleveland",
        "Hungary",
        "Switzerland",
        "VA Long Beach"
    ]
)

cp = st.selectbox(
    "Chest Pain Type",
    [
        "typical angina",
        "atypical angina",
        "non-anginal",
        "asymptomatic"
    ]
)

trestbps = st.number_input(
    "Resting Blood Pressure",
    80,
    250,
    120
)

chol = st.number_input(
    "Cholesterol",
    100,
    600,
    200
)

fbs = st.selectbox(
    "Fasting Blood Sugar",
    [True, False]
)

restecg = st.selectbox(
    "ECG Result",
    [
        "normal",
        "lv hypertrophy",
        "st-t abnormality"
    ]
)

thalch = st.number_input(
    "Maximum Heart Rate",
    60,
    220,
    150
)

exang = st.selectbox(
    "Exercise Induced Angina",
    [True, False]
)

oldpeak = st.number_input(
    "Old Peak",
    0.0,
    10.0,
    1.0
)

slope = st.selectbox(
    "Slope",
    [
        "upsloping",
        "flat",
        "downsloping"
    ]
)

# ----------------------------
# PREDICT
# ----------------------------

if st.button("❤️ Predict Disease"):

    patient = pd.DataFrame({

        "age":[age],
        "sex":[sex],
        "dataset":[dataset],
        "cp":[cp],
        "trestbps":[trestbps],
        "chol":[chol],
        "fbs":[fbs],
        "restecg":[restecg],
        "thalch":[thalch],
        "exang":[exang],
        "oldpeak":[oldpeak],
        "slope":[slope]

    })

    # Encode categorical columns
    categorical_columns = [
        "sex",
        "dataset",
        "cp",
        "restecg",
        "slope"
    ]

    for col in categorical_columns:
        patient[col] = label_encoders[col].transform(patient[col])

    # Scale
    patient_scaled = scaler.transform(patient)

    # Prediction
    prediction = model.predict(patient_scaled)[0]

    labels = {
        0: "🟢 Healthy",
        1: "🟡 Mild Heart Disease",
        2: "🟠 Moderate Heart Disease",
        3: "🔴 Severe Heart Disease",
        4: "🚨 Very Severe Heart Disease"
    }

    st.success(f"Prediction : {labels[prediction]}")