import streamlit as st


st.set_page_config(
    page_title="Model Information",
    page_icon="🤖",
    layout="wide"
)


def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


# -------------------------
# Title
# -------------------------

st.title("🤖 Machine Learning Model Information")

st.markdown("""
This page explains the machine learning approach used for diamond price prediction,
including model selection, optimization, and final performance.
""")


st.divider()


# -------------------------
# Selected Model Card
# -------------------------

st.header("🏆 Selected Final Model")


col1, col2 = st.columns([1,2])


with col1:

    st.markdown(
    """
    <div class="card">

    <h2 style="text-align:center;">
    🚀 XGBoost
    </h2>

    <p style="text-align:center;">
    Regression Model
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


with col2:

    st.markdown(
    """
    <div class="card">

    <h3>Why XGBoost?</h3>

    ✔ High prediction accuracy  
     
    ✔ Handles complex relationships  
     
    ✔ Works well with structured datasets  
     
    ✔ Reduces overfitting using regularization  

    </div>
    """,
    unsafe_allow_html=True
    )


st.divider()


# -------------------------
# Performance Metrics
# -------------------------

st.header("📊 Final Performance")


m1,m2,m3,m4 = st.columns(4)


with m1:
    st.metric(
        "R² Score",
        "98.25%"
    )


with m2:
    st.metric(
        "RMSE",
        "527.13"
    )


with m3:
    st.metric(
        "MAE",
        "276.37"
    )


with m4:
    st.metric(
        "Models Tested",
        "12"
    )


st.divider()


# -------------------------
# Hyperparameter tuning
# -------------------------

st.header("⚙ Hyperparameter Optimization")


st.markdown(
"""
<div class="card">

The XGBoost model was optimized using **RandomizedSearchCV**.

<h4>Tuned Parameters:</h4>

• n_estimators  
• learning_rate  
• max_depth  
• subsample  
• colsample_bytree  


<h4>Validation Method:</h4>

• 5-Fold Cross Validation  
• R² Score as optimization metric

</div>
""",
unsafe_allow_html=True
)



st.divider()


# -------------------------
# Model Explanation
# -------------------------

st.header("🧠 How XGBoost Works")


st.markdown(
"""
<div class="card">

XGBoost is an ensemble learning algorithm based on decision trees.

It builds multiple weak learners sequentially, where each new tree
focuses on correcting previous errors.

Advantages:

✔ Captures nonlinear patterns

✔ Handles feature interactions

✔ Provides strong predictive performance

</div>
""",
unsafe_allow_html=True
)



st.divider()


# Footer

st.markdown(
"""
<div class="footer">

💎 Diamond Price Prediction System  
Powered by XGBoost & Streamlit

</div>
""",
unsafe_allow_html=True
)