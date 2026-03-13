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
    <div style="text-align: center; color: #555; margin-bottom: 20px; font-size : 17px">
        This model can predict <b>second hand motorcycle price</b>, I use Voting Regressor <b>(Ensemble Learning)</b> which 
        combines multiple algorithms to provide the most stable price estimation <b>(LinearRegression,
         RandomForestRegressor and XGBRegressor)</b> with <b>78%</b> in R2 score.
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
    st.info("Use dataset from Kaggle, Dataset name **Motorcycle Dataset** by Nehal Birla and 1 collaborator Updated 6 years ago")
    st.image("asset/motocycle_dataset.jpg.")
    st.link_button("Visit dataset ➡️", "https://www.kaggle.com/datasets/nehalbirla/motorcycle-dataset")

with col2 :
    st.markdown(
        """
        <div style="text-align: left ; padding-bottom: 20">
            <p style="font-size: 30px; font-weight: bold; margin-bottom: 0;">
                📁 Feature
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.success(
        f"""
            **name** : Name of the motorcycle.

            **selling_price** : Price at which seller is selling the motorcycle.

            **year** : Year in which bike was bought.

            **seller type** : Tells if a Seller is Individual or a Dealer.

            **owner** : Number of previous owners of the vehicle.

            **km_driven** : Number of kilometre motorcycle has traveled.

            **ex_showroom_price** : Showroom price of the motorcycle.
        """
    )

st.divider()

st.markdown(
    """
    <div style="text-align: center; padding-bottom: 10px;">
        <p style="font-size: 30px; font-weight: bold; margin-bottom: 0;">
            📝 Data Preparation
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="text-align: left; color: #555; margin-bottom: 20px; font-size : 15px">
        <br>After check dataset, I saw have <b>null column</b> and <b>duplicates data</b>, That we need to <b>fill null column by median</b> in 
        ex_showroom_price column, And <b>drop duplicates data</b> to make sure model not <b>bias</b> by duplicates data.
    </div>
    """,
    unsafe_allow_html=True
)
st.code("""df.drop_duplicates(inplace=True)
df['ex_showroom_price'] = df['ex_showroom_price'].fillna(df['ex_showroom_price'].median())"""
)

st.markdown(
    """
    <div style="text-align: left; color: #555; margin-bottom: 20px; font-size : 15px">
        Convert year in <b>C.S.</b> (ex 2016) <b>to numerical</b> minus by current yesr (2026) .
    </div>
    """,
    unsafe_allow_html=True
)
st.code("""df['bike_age'] = 2026 - df['year']
df.drop('year', axis=1, inplace=True)"""
)

st.markdown(
    """
    <div style="text-align: left; color: #555; margin-bottom: 20px; font-size : 15px">
        <b>Convert</b> owner_dict in <b>category</b> (ex 1st owner) <b>to numerical</b> (ex 1, 2, ... ) .
    </div>
    """,
    unsafe_allow_html=True
)
st.code("""owner_dict = {'1st owner' : 1, '2nd owner' : 2, '3rd owner' : 3, '4th owner' : 4}
df['owner'] = df['owner'].map(owner_dict).fillna(5)"""
)

st.markdown(
    """
    <div style="text-align: left; color: #555; margin-bottom: 20px; font-size : 15px">
        <b>One-Hot Encoding</b> for seller_type (ex Individual, Dealer) to numerical (0, 1) .
    </div>
    """,
    unsafe_allow_html=True
)
st.code("df = pd.get_dummies(df, columns=['seller_type'], drop_first=True)")

st.markdown(
    """
    <div style="text-align: left; color: #555; margin-bottom: 20px; font-size : 15px">
        <b>Drop name</b> column because to many to classified.
    </div>
    """,
    unsafe_allow_html=True
)
st.code("df_final = df.drop('name', axis=1)")

st.divider()

st.markdown(
    """
    <div style="text-align: center; padding-bottom: 10px;">
        <p style="font-size: 30px; font-weight: bold; margin-bottom: 0;">
            👾 Model
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

import joblib
import pandas as pd

@st.cache_resource
def load_model () :
    return joblib.load("model/bike_price_predict.pkl")

model = load_model()

col1, col2 = st.columns(2)

with col1 :
    owner = st.selectbox("Owner (ex. 2 for Second-hand)", [1, 2, 3, 4, 5])
    km_driven = st.number_input("Kilometers Driven", min_value=0, value=5000)
    year = st.number_input("Age of motorcycle", min_value=0, max_value=50, value=5)

with col2 :
    ex = st.number_input("Ex-Showroom Price (THB)", value=50000)
    ex_price = ex * 2.40
    seller_choice = st.selectbox("Seller Type", ["Individual", "Dealer"])
    seller_type_individual = 1 if seller_choice == "Individual" else 0

col1, col2, col3 = st.columns([2, 1, 2])

with col2 :
    if st.button("Predict Price") :
        input_data = [[owner, km_driven, ex_price, year, seller_type_individual]]
        prediction = model.predict(input_data)
    
        predicted_thb = prediction[0] / 2.40
        final_price = predicted_thb

        if owner > 1:
            final_price = final_price * (1 - (owner * 0.05))

        if km_driven > 50000:
            final_price = final_price * 0.90
        
        max_limit = ex * 0.90 
        
        if final_price > max_limit:
            final_price = max_limit * 0.93

        st.success(f"Selling Price: \n\n **{final_price:,.0f}** THB")