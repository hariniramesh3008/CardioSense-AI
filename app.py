import streamlit as st

st.set_page_config(
    page_title="CardioSense AI",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("❤️ CardioSense AI")

st.subheader("AI Powered Heart Disease Severity Prediction System")

st.markdown("---")

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
## Welcome to CardioSense AI

CardioSense AI is an AI-powered healthcare application that predicts the severity of heart disease using Machine Learning.

### Features

- 🤖 XGBoost Machine Learning Model
- ❤️ Heart Disease Severity Prediction
- 📊 Interactive Dashboard
- 📈 Model Performance
- 📄 Download Patient Report
- 🧠 Explainable AI

---

### Workflow

Patient Data ➜ Data Processing ➜ XGBoost ➜ Prediction ➜ Report

👈 Use the **sidebar** to navigate through the application.
""")

with col2:
    st.metric("Patients", "920")
    st.metric("Features", "12")
    st.metric("Best Model", "XGBoost")
    st.metric("Accuracy", "58.2%")

st.success("✅ CardioSense AI Loaded Successfully")