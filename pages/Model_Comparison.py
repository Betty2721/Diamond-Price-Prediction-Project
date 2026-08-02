import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="Model Comparison",
    page_icon="📈",
    layout="wide"
)


# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


# Title
st.title("📈 Regression Model Comparison")

st.markdown("""
This page presents the performance comparison of all regression algorithms
evaluated for diamond price prediction.
""")


st.divider()


# -----------------------------------
# Model Results
# -----------------------------------

comparison_df = pd.DataFrame({

    "Algorithm":[
        "Linear Regression",
        "Ridge",
        "Lasso",
        "Decision Tree",
        "Random Forest",
        "Gradient Boosting",
        "SVR",
        "Extra Trees",
        "AdaBoost",
        "XGBoost",
        "LightGBM",
        "CatBoost"
    ],

    "MAE":[
        858.71,
        858.80,
        859.68,
        355.64,
        267.98,
        364.87,
        1346.84,
        263.97,
        1296.37,
        276.37,
        284.86,
        316.76
    ],


    "RMSE":[
        1351.26,
        1351.26,
        1351.38,
        729.03,
        542.05,
        655.69,
        2778.03,
        543.43,
        1536.30,
        527.13,
        536.63,
        581.41
    ],


    "R² Score":[
        0.8851,
        0.8851,
        0.8851,
        0.9666,
        0.9815,
        0.9730,
        0.5145,
        0.9814,
        0.8515,
        0.9825,
        0.9819,
        0.9787
    ]


})


# -----------------------------------
# Highlight Best Model
# -----------------------------------

st.header("🏆 Best Performing Model")


col1, col2, col3 = st.columns(3)


with col1:
    st.metric(
        "Best Model",
        "XGBoost"
    )


with col2:
    st.metric(
        "Highest R²",
        "98.25%"
    )


with col3:
    st.metric(
        "Lowest RMSE",
        "527.13"
    )



st.divider()



# -----------------------------------
# Table
# -----------------------------------

st.header("📋 Complete Performance Table")


st.dataframe(
    comparison_df.style.highlight_max(
        subset=["R² Score"],
        color="#bbf7d0"
    ),
    use_container_width=True
)



st.divider()



# -----------------------------------
# R2 Chart
# -----------------------------------

st.header("📊 R² Score Comparison")


r2_fig = px.bar(

    comparison_df.sort_values(
        "R² Score",
        ascending=False
    ),

    x="Algorithm",

    y="R² Score",

    text="R² Score",

    title="Model Accuracy Ranking"

)


r2_fig.update_traces(
    texttemplate="%{text:.4f}",
    textposition="outside"
)


st.plotly_chart(
    r2_fig,
    use_container_width=True
)



st.divider()



# -----------------------------------
# RMSE Chart
# -----------------------------------

st.header("📉 RMSE Comparison")


rmse_fig = px.bar(

    comparison_df.sort_values(
        "RMSE"
    ),

    x="Algorithm",

    y="RMSE",

    text="RMSE",

    title="Prediction Error Comparison"

)


rmse_fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)


st.plotly_chart(
    rmse_fig,
    use_container_width=True
)



st.divider()



# -----------------------------------
# Explanation
# -----------------------------------

st.header("💡 Model Selection Explanation")


st.markdown(
"""
<div class="card">

XGBoost Regression was selected as the final model because it achieved the
best overall performance.

<strong>Reasons:</strong>

<br>

✔ Highest R² Score (0.9825)

<br>

✔ Lowest RMSE (527.13)

<br>

✔ Strong ability to learn complex relationships

<br>

✔ Good generalization performance

<br>

✔ Effective for structured datasets

</div>
""",
unsafe_allow_html=True
)



# Footer

st.markdown(
"""
<div class="footer">

💎 Diamond Price Prediction System  
Machine Learning Regression Application

</div>
""",
unsafe_allow_html=True
)