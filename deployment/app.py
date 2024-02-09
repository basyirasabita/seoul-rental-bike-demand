# import Libraries
import streamlit as st

# import EDA and prediction pages
import eda, prediction

# Set page config
st.set_page_config(
    page_title = 'Rented Bike Demand in Seoul',
    initial_sidebar_state = 'expanded'
)

# Navigation bar
page = st.sidebar.selectbox('Choose Page', ('Predictor', 'EDA'))

# Navigate run function
if page == 'EDA':
    eda.run()
else:
    prediction.run()