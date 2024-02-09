# Import Library
import streamlit as st
import pandas as pd
import numpy as np 
import feature_engine
import warnings
warnings.filterwarnings('ignore')

import pickle

# Import Model
with open('model_gbm_reg.pkl', 'rb') as file:
    model = pickle.load(file)

# Function for running
def run():
    # Set title
    st.title('Seoul Rented Bike Count Predictor')

    # Set subheader
    st.subheader('This page will provide you form to predict Rented Bike Count on a certain date and weather conditions')
    st.markdown('---')

    # Image
    st.image('https://img.freepik.com/free-photo/vintage-gray-bicycle-outdoors_23-2148907987.jpg?w=1480&t=st=1707387048~exp=1707387648~hmac=94be620774536b18275810656497255459c6ee62fa86343f7231eff16388f796', caption='Image by Freepik')
    st.markdown('---')

    # Form for Inference Data
    st.markdown('## Input Data')
    with st.form('form_rented_bike_count'):
        date = st.date_input("Date :date:") 
        hour = st.number_input('Hour :hourglass_flowing_sand:', min_value = 0, max_value = 23, step=1)
        temperature = st.number_input('Temperature (C) :thermometer:', min_value = -20.0, max_value = 40.0, step=0.1)
        humidity = st.number_input('Humidity (%) :droplet:', min_value = 0, max_value = 100, step = 1)
        windSpeed = st.number_input('Wind Speed (m/s) :wind_blowing_face:', min_value = 0.0, max_value = 10.0, step = 0.1) 
        visibility = st.number_input('Visibility (10m) :eyes:', min_value = 0, max_value = 2000, step = 1)
        dewPointTemperature = st.number_input('Dew Point Temperature (C) :droplet:', min_value = -30.0, max_value = 30.0, step=0.1)
        solarRadiation = st.number_input('Solar Radiation (MJ/m2) :sunny:', min_value = 0.00, max_value = 20.00, step = 0.01)
        rainfall = st.number_input('Rainfall (mm) :umbrella_with_rain_drops:', min_value = 0.0, max_value = 50.0, step = 0.1)
        snowfall = st.number_input('Snowfall (cm) :snowflake:', min_value = 0.0, max_value = 30.0, step = 0.1)
        seasons = st.selectbox(
            'Seasons',
            options = ['Spring', 'Summer', 'Autumn','Winter']
        )
        holiday = st.radio(
            'Holiday',
            options = ['Holiday', 'No Holiday']
        ) 
        functioningDay = st.radio(
            'Functioning Day',
            options = ['Yes', 'No']
        ) 
        st.markdown('---')
        submitted = st.form_submit_button()

    data_inf = {
        'Date': date, 
        'Hour': hour,
        'Temperature': temperature, 
        'Humidity': humidity,
        'Wind Speed': windSpeed, 
        'Visibility': visibility, 
        'Dew Point Temperature': dewPointTemperature, 
        'Solar Radiation': solarRadiation,
        'Rainfall': rainfall, 
        'Snowfall': snowfall, 
        'Seasons': seasons, 
        'Holiday': holiday, 
        'Functioning Day': functioningDay
    }

    df_inf = pd.DataFrame([data_inf])

    if submitted:
        st.markdown('Submitted Data:')
        st.dataframe(df_inf)
        st.markdown('---')
        score = model.predict(df_inf)

        st.markdown(f'Predicted Bike Rented Count on {df_inf.Date.loc[0]} ({df_inf.Seasons.loc[0]}): **{round(score[0], 0)}**')

    st.text('Basyira Sabita - 2024')

if __name__=='__main__':
    run()