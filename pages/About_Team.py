import streamlit as st

st.set_page_config(
    page_title="About Team",
    page_icon="👥",
    layout="wide"
)

# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.title("👥 About the Team")

st.markdown("""
This project was developed as part of a **Machine Learning Regression Project** focusing on predicting diamond prices using multiple regression algorithms.
""")

st.divider()

# Team Information
st.header("🎓 Team Information")

col1, col2 = st.columns(2)

with col1:
    st.info("""
**Project Title**

Diamond Price Prediction Using Machine Learning
""")

    st.info("""
**Course**

Machine Learning
""")

with col2:
    st.info("""
**Regression Models Evaluated**

12 Models
""")

    st.info("""
**Best Model**

🏆 XGBoost Regression
""")

st.divider()

# Technologies
st.header("💻 Technologies Used")

st.markdown("""
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Streamlit
- Plotly
- Matplotlib
- Seaborn
""")

st.divider()

# Workflow
st.header("📌 Project Workflow")

st.markdown("""
✔ Data Cleaning

✔ Exploratory Data Analysis

✔ Data Preprocessing

✔ Feature Engineering

✔ Model Training

✔ Model Evaluation

✔ Hyperparameter Tuning

✔ Web Application Development

✔ Streamlit Deployment
""")

st.divider()

# Acknowledgement
st.header("🙏 Acknowledgement")

st.success("""
Thank you for exploring our Diamond Price Prediction application.

This project demonstrates the complete machine learning workflow—from data preprocessing and model development to evaluation and deployment using Streamlit.
""")

st.markdown("---")

st.markdown(
"""
<div class="footer">

💎 Diamond Price Prediction System  
Built with Python | XGBoost | Streamlit

</div>
""",
unsafe_allow_html=True
)