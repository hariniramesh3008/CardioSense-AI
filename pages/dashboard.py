import streamlit as st
import pandas as pd

st.title("📊 Dashboard")

df = pd.read_csv("data/heart_disease_uci.csv")

st.dataframe(df.head())

st.write("Dataset Shape:", df.shape)