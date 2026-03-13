import streamlit as st

if st.button("⬅️ Back") :
    st.switch_page("main.py")

st.markdown(
    """
    <div style="text-align: center; padding-bottom: 10px;">
        <p style="font-size: 30px; font-weight: bold; margin-bottom: 0;">
            🧠 Cloud Classification
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: center; color: #555; margin-bottom: 20px; font-size : 17px">
        This model can <b>classified</b> clouds in the sky ex. clear sky, cumulus clouds and other. Use <b>CNN</b> 
        (Convolutional <b>Neural Network</b>) for this model with accuracy <b>83.12%</b> and evaluate <b>83.33%</b>
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

st.markdown(
        """
        <div style="text-align: center ; padding-bottom: 20">
            <p style="font-size: 30px; font-weight: bold; margin-bottom: 0;">
                🛢️ Dataset
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
st.info("Use dataset from Kaggle, Dataset name **Clouds Photos** by Omar Essa Updated 6 months ago")
st.image("asset/cloud-dataset.png")

col1, col2, col3 = st.columns([1.93, 1, 2])

with col2 :
    st.link_button("Visit dataset ➡️", "https://www.kaggle.com/datasets/jockeroika/clouds-photos")

st.divider()

import tensorflow as tf
from PIL import Image
import numpy as np

@st.cache_resource
def load_my_model () :
    return tf.keras.models.load_model('model/clouds-classification_final.h5')

model = load_my_model()
class_names = ['cirriform clouds', 'clear sky', 'cumulonimbus clouds', 'cumulus clouds', 'high cumuliform clouds', 'stratiform clouds', 'stratocumulus clouds']

file = st.file_uploader("Upload cloud photo . . . ", type=["jpg", "jpeg", "png"])

if file :
    img = Image.open(file).convert('RGB')
    st.image(img, caption="Target Image", use_container_width=True)

    img_resized = img.resize((224, 224))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2 :

        st.markdown("""
        <style>
        .stButton button {
            display: block;
            margin: 0 auto;
        }
        </style>
        """, unsafe_allow_html=True)

        if st.button("Classify") :
            res = model.predict(img_array)
            score = tf.nn.softmax(res[0])
            label = class_names[np.argmax(score)]

            st.success(f"**Result:** {label}")
            st.info(f"**Confidence:** {100 * np.max(score):.2f}%")