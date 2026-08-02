import streamlit as st
import pandas as pd
import joblib

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="Predict Diamond Price",
    page_icon="💰",
    layout="wide"
)

# ----------------------------------
# Load CSS
# ----------------------------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ----------------------------------
# Title
# ----------------------------------
st.title("💰 Diamond Price Prediction")
st.write("Enter the diamond characteristics below to estimate the market price of a diamond.")

# ----------------------------------
# Load Model & Encoder
# ----------------------------------
model = joblib.load("models/xgboost_model.pkl")
encoder = joblib.load("models/ordinal_encoder.pkl")

# ----------------------------------
# Input Form
# ----------------------------------
st.header("💎 Diamond Information")

col1, col2 = st.columns(2)

with col1:

    carat = st.number_input(
        "Carat",
        min_value=0.10,
        max_value=5.00,
        value=1.00,
        step=0.01
    )

    cut = st.selectbox(
        "Cut",
        ["Fair", "Good", "Very Good", "Premium", "Ideal"]
    )

    color = st.selectbox(
        "Color",
        ["D", "E", "F", "G", "H", "I", "J"]
    )

    clarity = st.selectbox(
        "Clarity",
        ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
    )

with col2:

    depth = st.number_input(
        "Depth",
        value=61.5
    )

    table = st.number_input(
        "Table",
        value=57.0
    )

    x = st.number_input(
        "Length (x)",
        value=5.70
    )

    y = st.number_input(
        "Width (y)",
        value=5.70
    )

    z = st.number_input(
        "Depth (z)",
        value=3.50
    )

# ----------------------------------
# Predict Button
# ----------------------------------
predict = st.button("💎 Predict Price")

# ----------------------------------
# Prediction
# ----------------------------------
if predict:

    # Create DataFrame
    input_df = pd.DataFrame({

        "carat":[carat],
        "cut":[cut],
        "color":[color],
        "clarity":[clarity],
        "depth":[depth],
        "table":[table],
        "x":[x],
        "y":[y],
        "z":[z]

    })

    # Encode categorical features
    categorical_cols = ["cut","color","clarity"]

    input_df[categorical_cols] = encoder.transform(
        input_df[categorical_cols]
    )

    # ============================
    # IMPORTANT
    # If you trained XGBoost using
    # StandardScaler, load scaler.pkl
    # and uncomment these lines:
    #
    # scaler = joblib.load("models/scaler.pkl")
    # input_df = scaler.transform(input_df)
    # ============================

    # Prediction
    prediction = model.predict(input_df)

    predicted_price = prediction[0]

    # ----------------------------------
    # Display Result
    # ----------------------------------
    st.markdown("---")

    st.session_state["predicted_price"] = predicted_price

    st.success(
        "Prediction completed! Go to Prediction Result page."
    )
    st.markdown(
        f"""
        <div style="
            background:linear-gradient(135deg,#2563EB,#4F46E5);
            padding:30px;
            border-radius:15px;
            text-align:center;
            color:white;
            box-shadow:0px 5px 15px rgba(0,0,0,0.3);
        ">

        <h2>Estimated Diamond Price</h2>

        <h1 style="font-size:48px;">
        ${predicted_price:,.2f}
        </h1>

        <p>
        Prediction generated using the trained XGBoost Regression Model.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("Prediction completed successfully!")

    st.markdown(
"""
<div class="footer">

💎 Diamond Price Prediction System  
Built with Python | XGBoost | Streamlit

</div>
""",
unsafe_allow_html=True
)