import streamlit as st

st.set_page_config(
    page_title="Project Description",
    page_icon="📖",
    layout="wide"
)

def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("📖 Project Description")

st.markdown("""
## Overview

The Diamond Price Prediction System is a machine learning application that predicts the market price of a diamond based on its physical characteristics.

The project compares multiple regression algorithms to identify the most accurate model. After evaluation and hyperparameter tuning, XGBoost Regression was selected as the final model.

---

## Project Objectives

- Predict diamond prices accurately.
- Compare multiple regression algorithms.
- Evaluate models using MAE, MSE, RMSE, and R² Score.
- Deploy the best-performing model with Streamlit.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit
""")

st.markdown(
"""
<div class="footer">

💎 Diamond Price Prediction System  
Built with Python | XGBoost | Streamlit

</div>
""",
unsafe_allow_html=True
)