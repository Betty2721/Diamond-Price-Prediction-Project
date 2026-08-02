import streamlit as st


st.set_page_config(
    page_title="Prediction Result",
    page_icon="💎",
    layout="wide"
)


st.title("💎 Prediction Result")


if "predicted_price" in st.session_state:

    price = st.session_state["predicted_price"]


    st.markdown(
    f"""
    <div style="
    background:linear-gradient(135deg,#2563EB,#4F46E5);
    padding:30px;
    border-radius:15px;
    text-align:center;
    color:white;
    ">

    <h2>Estimated Diamond Price</h2>

    <h1>${price:,.2f}</h1>

    <p>
    Generated using XGBoost Regression Model
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


else:

    st.warning(
        "No prediction available. Please go to Prediction Form first."
    )

    st.markdown(
"""
<div class="footer">

💎 Diamond Price Prediction System  
Built with Python | XGBoost | Streamlit

</div>
""",
unsafe_allow_html=True
)