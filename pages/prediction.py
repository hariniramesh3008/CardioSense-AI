import streamlit as st

# ----------------------------
# PAGE SETTINGS
# ----------------------------

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="🩺",
    layout="wide"
)

# ----------------------------
# TITLE
# ----------------------------

st.title("🩺 Heart Disease Prediction")

st.markdown("""
This page is under testing.

If this page loads successfully in Streamlit Cloud, then the deployment issue is NOT in the page itself. We can then test the ML model files separately.
""")

# ----------------------------
# TEST MESSAGE
# ----------------------------

st.success("✅ Prediction page loaded successfully!")

# ----------------------------
# TEMPORARY TEST INPUTS
# ----------------------------

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=45
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

bp = st.number_input(
    "Blood Pressure",
    min_value=80,
    max_value=250,
    value=120
)

st.write("Age :", age)
st.write("Gender :", gender)
st.write("Blood Pressure :", bp)

# ----------------------------
# TEST BUTTON
# ----------------------------

if st.button("Test Prediction Page"):
    st.success("🎉 Prediction page is working correctly!")