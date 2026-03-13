import streamlit as st

st.markdown(
    """
    <div style="text-align: center; padding-bottom: 10px;">
        <p style="font-size: 45px; font-weight: bold; margin-bottom: 0;">
            Intelligent System Project
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: center; color: #555; margin-bottom: 20px; font-size : 15px">
        This website is designed for the presentation of the Intelligent System (IS) subject project. 
        It features a <b>Machine Learning (ML)</b> model and a <b>Neural Network (NN)</b> model, 
        organized into dedicated pages for each.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="text-align: left ; padding-bottom: 20">
            <p style="font-size: 30px; font-weight: bold; margin-bottom: 0;">
                📊 Price Prediction
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.info(
        """
        **Type:** Machine Learning (Regression)  
        Predicts the market value of second-hand motorcycles based on age, mileage, and other key features.
        """
    )
    if st.button("Open ML Model ➡️") :
        st.switch_page("pages/ml.py")

with col2:
    st.markdown(
        """
        <div style="text-align: left ; padding-bottom: 20">
            <p style="font-size: 30px; font-weight: bold; margin-bottom: 0;">
                🧠 Cloud Classification
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.success(
        """
        **Type:** Neural Network (Classification)  
        Classifies different types of clouds, such as clear sky or stratiform clouds, using computer vision.
        """
    )
    if st.button("Open NN Model ➡️") :
        st.switch_page("pages/nn.py")

st.divider()

st.markdown(
    """
    <div style="text-align: center; padding-top: 20px;">
        <p style="font-size: 14px; margin-bottom: 0; color: #666;">
            Prepared by
        </p>
        <p style="font-size: 22px; font-weight: bold; color: #337CE2; margin-top: 0; margin-bottom: 0;">
            Kajbundit Monta 👤
        </p>
            <p style="font-size: 14px; color: #666;">
            ID: 6704062617318 | Section 4
        </p>
    </div>
    """,
    unsafe_allow_html=True
)