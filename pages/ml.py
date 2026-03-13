import streamlit as st

if st.button("⬅️ Back") :
    st.switch_page("main.py")

st.markdown(
    """
    <div style="text-align: center; padding-bottom: 10px;">
        <p style="font-size: 30px; font-weight: bold; margin-bottom: 0;">
            📊 Motorcycle Price Prediction
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: center; color: #555; margin-bottom: 20px; font-size : 15px">
        This model can predict second hand motorcycle price ...
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

col1, col2 = st.columns(2)

with col1 :
    st.markdown(
        """
        <div style="text-align: left ; padding-bottom: 20">
            <p style="font-size: 30px; font-weight: bold; margin-bottom: 0;">
                🛢️ Dataset
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.info("Use dataset from Kaggle, Dataset name **Motorcycle Specifications Dataset** by Emmanuel F. Werr ")

with col2 :
    if (st.button("Dataset")) :
