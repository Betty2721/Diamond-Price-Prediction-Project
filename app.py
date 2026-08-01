import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Diamond Price Prediction",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("💎 Diamond Price Prediction")
st.sidebar.success("Select a page from the sidebar.")

st.sidebar.markdown("---")
st.sidebar.info(
    """
    Machine Learning Project

    Best Model:
    ✅ XGBoost Regression

    Dataset:
    Diamonds Dataset
    """
)

# -----------------------------
# Hero Section
# -----------------------------
st.title("💎 Diamond Price Prediction System")

st.subheader("Predict Diamond Prices Using Machine Learning")

st.write(
    """
This web application predicts the price of a diamond using an optimized
XGBoost Regression Model trained on the Diamonds dataset.

Navigate through the pages using the sidebar to learn about the project,
explore the dataset, compare models, and predict diamond prices.
"""
)

# -----------------------------
# Metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Dataset Size", "53,940")

with col2:
    st.metric("Features", "10")

with col3:
    st.metric("Models Tested", "12")

with col4:
    st.metric("Best Model", "XGBoost")

st.divider()

# -----------------------------
# Project Highlights
# -----------------------------
st.header("✨ Project Highlights")

c1, c2 = st.columns(2)

with c1:
    st.success("""
✔ Data Cleaning

✔ Exploratory Data Analysis

✔ Feature Engineering

✔ Model Training
""")

with c2:
    st.success("""
✔ 12 Regression Models

✔ Hyperparameter Tuning

✔ Streamlit Deployment

✔ Interactive Predictions
""")

st.divider()

# -----------------------------
# Workflow
# -----------------------------
st.header("📌 Project Workflow")

st.write("""
1. Data Collection

2. Data Cleaning

3. Exploratory Data Analysis

4. Data Preprocessing

5. Model Training

6. Model Evaluation

7. Hyperparameter Tuning

8. Model Deployment using Streamlit
""")

st.divider()

st.caption("Developed for the Machine Learning Regression Project")