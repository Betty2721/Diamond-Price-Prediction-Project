import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dataset Information",
    page_icon="📊",
    layout="wide"
)

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

df = pd.read_csv("data/diamonds.csv")

if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

st.divider()

# Dataset Statistics
st.header("📌 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Rows", f"{df.shape[0]:,}")

with col2:
    st.metric("Columns", df.shape[1])

with col3:
    st.metric("Missing Values", df.isnull().sum().sum())

st.divider()

# Dataset Preview
st.header("👀 Dataset Preview")

st.dataframe(df.head(10), use_container_width=True)

st.divider()

# Data Types
st.header("📋 Data Types")

dtype_df = pd.DataFrame({
    "Column": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(dtype_df, use_container_width=True)

st.divider()

# Feature Description
st.header("📖 Feature Description")

feature_df = pd.DataFrame({
    "Feature": [
        "carat",
        "cut",
        "color",
        "clarity",
        "depth",
        "table",
        "x",
        "y",
        "z",
        "price"
    ],

    "Description": [
        "Weight of the diamond",
        "Quality of the cut",
        "Diamond color grade",
        "Diamond clarity grade",
        "Total depth percentage",
        "Width of the top facet",
        "Length (mm)",
        "Width (mm)",
        "Depth (mm)",
        "Target variable (Price)"
    ]
})

st.dataframe(feature_df, use_container_width=True)

st.divider()

# Numerical Summary
st.header("📈 Summary Statistics")

st.dataframe(df.describe(), use_container_width=True)

st.markdown(
"""
<div class="footer">

💎 Diamond Price Prediction System  
Built with Python | XGBoost | Streamlit

</div>
""",
unsafe_allow_html=True
)