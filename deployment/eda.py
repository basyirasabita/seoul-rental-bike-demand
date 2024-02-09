# Import Library
import streamlit as st
import pandas as pd
import numpy as np 
import warnings
warnings.filterwarnings('ignore')

# Library for visualization
import matplotlib.pyplot as plt 
import seaborn as sns 

def run():
    # Set title
    st.title('Seoul Bike Demand Data Analysis')

    # Set subheader
    st.subheader('This page will display the EDA of the dataset')
    st.markdown('---')

    # Image
    st.image('https://img.freepik.com/free-photo/woman-riding-bike-city_23-2149318518.jpg?w=1800&t=st=1707383844~exp=1707384444~hmac=05ddc9504f8ce65efb9c1eb55a5b55515b8317333b6b06d6cb03167b19112679', caption='Image by Freepik')
    st.markdown('---')

    # Dataframe
    st.markdown('## Dataframe Seoul Bike Demand')
    data = pd.read_csv("SeoulBikeDataCleaned.csv")
    data['Date'] = pd.to_datetime(data['Date'], format='%Y-%m-%d')

    # Dict for defining the new column names
    new_cols = {
        'Temperature(C)': 'Temperature',
        'Humidity(%)': 'Humidity',
        'Wind speed (m/s)': 'Wind Speed',
        'Visibility (10m)': 'Visibility',
        'Dew point temperature(C)': 'Dew Point Temperature',
        'Solar Radiation (MJ/m2)': 'Solar Radiation',
        'Rainfall(mm)': 'Rainfall',
        'Snowfall (cm)': 'Snowfall'
    }

    # Rename the columns with new column names
    data = data.rename(columns = new_cols)
    st.dataframe(data.head(24))

    # EDA
    st.markdown('---')
    st.markdown('## Exploratory Data Analysis (EDA)')
    st.markdown('---')

    # Plot Distribution
    distribution = {
        'Rented Bike Count': 'The `Rented Bike Count` column exhibits a positively skewed distribution, suggesting that the data is skewed to the left. The boxplot reveals numerous outliers in this column, with values exceeding 3500 bike rentals. It is assumed that these outliers occur due to specific events throughout the year, such as public holidays, which would naturally affect bike rental counts, leading to fluctuations. Typically, the bike rental count peaks within the range of 0 to 500 rentals.', 
        'Temperature': 'The `Temperature` column shows a normal distribution, indicating that the mean, median, mode value is similar and the data is pooled around the center. As observed in the boxplot, there are no outliers detected in this column. Moreover, the temperature values range from -20°C to 40°C, covering a wide span. This range indicates that the data encompasses the four seasons.', 
        'Humidity': 'The `Humidity` column shows a normal distribution, indicating that the mean, median, mode value is similar and the data is pooled around the center but slightly lean to the right. As observed in the boxplot, there are no outliers detected in this column. Moreover, we note that the data values range between 0% and 100%. The peaks of humidity in Seoul throughout the year fall within the range of 40% to 60%, indicating moderate humidity levels in the city.',
        'Wind Speed': 'The `Wind Speed` column shows a positive skewness distribution, indicating that the data is skewed towards the left. As observed in the boxplot, there are quite a lot of outliers in this column, with values significantly exceeding 7 m/s. Notably, the peak wind speed in Seoul throughout the year is around 1 m/s which we can infer as light breeze.', 
        'Visibility': 'The `Visibility` column shows a negative skewness distribution, indicating that the data is skewed towards the right. As observed in the boxplot, there are no outliers detected in this column, with values ranging from 0 to 20000 m of visibility. The visibility peaks in 20000 m or 20 km which considered as excellent visibility.', 
        'Dew Point Temperature': 'The `Dew Point Temperature` column shows a normal distribution, indicating that the mean, median, mode value is similar and the data is pooled around the center but slightly leans to the right. As observed in the boxplot, there are no outliers detected in this column. Additionally, we observe that the data values range between -30°C and 30°C.',
        'Solar Radiation': 'The `Solar Radiation` column shows a high positive skewness distribution, indicating that the data is skewed towards the left. As observed in the boxplot, there are a lot of outliers in this column, with values significantly exceeding 3.5 MJ/m2. Interestingly, solar radiation in Seoul throughout the year peaks at 0, indicating no solar radiation on a daily basis. However, considering that the dataset includes nighttime data as well, this explains why the solar radiation peaks at 0.', 
        'Rainfall': 'The `Rainfall` column shows a high positive skewness distribution, indicating that the data is skewed towards the left. As observed in the boxplot, there are numerous outliers in this column, with values significantly reaching 35 mm. Interestingly, rainfall in Seoul is mostly minimal, as indicated by the frequent occurrence of 0 mm data throughout the year. The most precipitation in the dataset period is nearly 35 mm which considered as moderate rain. However, the dataset also captures instances of moderate rainfall, with the highest recorded precipitation being nearly 35 mm.', 
        'Snowfall': 'The `Snowfall` column shows a high positive skewness distribution, indicating that the data is skewed towards the left. As observed in the boxplot, there are numerous outliers in this column, with values significantly exceeding 8 cm. The data is predominantly clustered around 0, which aligns with the presence of all four seasons in the dataset, and snowfall typically occurring only during winter.', 
        'Seasons': 'The `Seasons` column contains 4 unique values: Spring, Summer, Autumn, and Winter. Each season accounts for approximately 25% of the data, indicating a balanced proportion. From this visualization, we can infer that the dataset consists of data for a single year (1 cycle of 4 seasons).',
        'Holiday': 'The `Holiday` column contains 2 unique values: Holiday and No Holiday. The percentage of "No Holiday" values (95.1%) is significantly higher than the percentage of "Holiday" values (4.9%), indicating an imbalanced proportion. This proportion makes sense as there are typically more non-holiday days in a year.', 
        'Functioning Day': 'The `Functioning Day` column contains 2 unique values: Yes and No. The percentage of "Yes" values (96.6%) is significantly higher than the percentage of "No" values (3.4%), indicating an imbalanced proportion. This proportion makes sense as there are typically more functioning days in a year.'
    }
    # Select the column
    st.markdown('### Data Distribution')
    column = st.selectbox(
        'Choose Column',
        [
            'Rented Bike Count', 
            'Temperature', 
            'Humidity',
            'Wind Speed', 
            'Visibility', 
            'Dew Point Temperature',
            'Solar Radiation', 
            'Rainfall', 
            'Snowfall', 
            'Seasons',
            'Holiday', 
            'Functioning Day'
        ],
        index=None,
        placeholder='Choose Column'
    )

    if column == None:
        st.markdown('Please Choose the Column First to See Visualization')
    elif column == 'Seasons' or column == 'Holiday' or column == 'Functioning Day':
        labels = data[column].value_counts().index.tolist()
        sizes = data[column].value_counts().values.tolist()

        canvas = plt.figure(figsize=(12,5))

        # Barplot
        plt.subplot(1, 2, 1)
        sns.barplot(x=labels, y=sizes)
        plt.title('Bar Chart')

        # Piechart
        plt.subplot(1, 2, 2)
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Pie Chart')

        st.pyplot(canvas)
        st.markdown(distribution[column])
    else:
        st.markdown(f'{column} Distribution')
        canvas = plt.figure(figsize=(12,5))

        # Plot Histogram
        plt.subplot(1, 2, 1)
        sns.histplot(data=data[column], kde=True, color='plum', bins=20)
        plt.title('Histogram')

        # Boxplot
        plt.subplot(1, 2, 2)
        sns.boxplot(data=data, x=column, color='plum')
        plt.title('Boxplot')

        st.pyplot(canvas)
        st.markdown(distribution[column])
    
    st.markdown('---')

    # Plot Rented Bike Count by Seasons and Months
    # Group raw data by Date
    rent_bike_date_df = data.groupby('Date').agg({'Rented Bike Count': 'mean', 'Seasons': 'first'}).reset_index()

    # Extract month from Date
    rent_bike_date_df['Month'] = rent_bike_date_df['Date'].dt.month

    # Group data by Month
    rent_bike_month_df = rent_bike_date_df.groupby('Month').agg({'Rented Bike Count': 'mean', 'Seasons': 'first'}).reset_index()

    # Declare the figure size
    canvas = plt.figure(figsize=(10,5))

    # Barplot the rented bike count by month
    st.markdown('### Rented Bike Count by Seasons and Months')
    sns.barplot(
        rent_bike_month_df, 
        x = 'Month', 
        y = 'Rented Bike Count',
        hue = 'Seasons',
        palette=['cornflowerblue', 'palevioletred', 'gold', 'darkorange']
    )

    st.pyplot(canvas)
    st.markdown('The peak of bike rental demand occurs during Summer (Months 6 to 8). Demand in Spring (Months 3 to 5) and Autumn (Months 9 to 11) is relatively similar. Meanwhile, the lowest bike rental demand is observed in Winter (Months 12 to 2). There is a notable difference between the highest and lowest demand periods. Based on these findings, we can infer a correlation between bike rental demand and temperature. As seen in the visualization, demand decreases as temperatures drop.')

    st.markdown('---')

    # Plot Rented Bike Count by Temperatures
    # Slicing the Data
    rent_bike_temp_df = data[['Rented Bike Count', 'Temperature']]

    # Adding temperature category
    bins = pd.cut(rent_bike_temp_df['Temperature'], bins=5, labels=['Very Cold', 'Cold', 'Moderate', 'Warm', 'Hot'])
    rent_bike_temp_df['Temperature Level'] = bins

    # Group by Temperature Level
    rent_bike_temp_grouped_df = rent_bike_temp_df.groupby('Temperature Level') \
                                .agg({'Rented Bike Count': 'mean', 'Temperature': 'mean'}).sort_values('Temperature', ascending=False) \
                                .reset_index()
    
    # Declare the figure size
    canvas = plt.figure(figsize=(10,5))

    # Scatterplot the rented bike count by temperature
    st.markdown('### Rented Bike Count by Temperatures')

    sns.lineplot(
        rent_bike_temp_grouped_df, 
        x = 'Temperature', 
        y = 'Rented Bike Count',
        color='darkmagenta',
        marker='D'
    )

    st.pyplot(canvas)
    st.markdown('As previously mentioned, according to this visualization, we can observe an increase in bike rental demand with higher temperatures. The lowest demand is less than 200 rentals, while the highest demand exceeds 1000 rentals. We can also see that there is a significant increase in demand as temperatures transition from cold (approx. 0°C) to warm (approx. 20°C).')
    
    st.markdown('---')

    # Plot Rented Bike Demand by Weekend or Weekdays
    # Slicing raw data
    rent_bike_days_hour_df = data[['Date', 'Rented Bike Count', 'Hour']]

    is_weekend = []
    for date in rent_bike_days_hour_df['Date']:
        dow = date.day_of_week
        if dow >= 5:
            is_weekend.append('Weekend')
        else:
            is_weekend.append('Weekday')

    rent_bike_days_hour_df['Days'] = is_weekend

    # Declare the figure size
    canvas = plt.figure(figsize=(10,5))

    # Barplot the rented bike count by month
    st.markdown('### Rented Bike Count by Weekend or Weekdays')

    sns.barplot(
        rent_bike_days_hour_df, 
        x = 'Days', 
        y = 'Rented Bike Count',
        palette = ['royalblue', 'tomato']
    )

    st.pyplot(canvas)
    st.markdown('According to the visualization, bike rental demand is higher on weekdays than weekends. Based on domain knowledge, we infer that weekday demand is elevated due to bike usage for commuting to and from work. Meanwhile, in weekends we see lower demand as bikes are more commonly used for recreational purposes. Surprisingly, the observed difference in bike rental counts between weekdays and weekends is not that extensive, indicating that demand for recreational purposes may also be significant, contributing to overall rental demand.')

    st.markdown('---')
    
    # Plot Rented Bike Count by Hour
    # Declare the figure size
    canvas = plt.figure(figsize=(15,7))

    # Barplot the rented bike count by hour
    st.markdown('### Rented Bike Count by Hour')

    sns.barplot(
        rent_bike_days_hour_df, 
        x = 'Hour', 
        y = 'Rented Bike Count',
        hue = 'Days',
        palette=['royalblue', 'tomato']
    )

    st.pyplot(canvas)
    st.markdown('After plotting the demand distribution on weekdays and weekends, we can now analyze the distribution by hour. We observe that bike rentals peak at 8 AM and 6 PM, aligning with rush hours, backing up the assumption of people rent a bike on weekdays for commuting purposes. Weekday demand rises from 4 AM to 8 AM, drops significantly thereafter, then increases again from 10 AM, reaching its peak at 6 PM. After 6 PM, the demand declines until 4 AM. Surprisingly, demand remains unexpectedly high in the evenings and after midnight on weekdays. On weekends, demand steadily increases from 5 AM, reaching its peak at 5 PM, then gradually decreases until 5 AM.')

    st.markdown('---')

    # Plot 
    # Defining all the numeric columns in data
    num_cols_raw = data.select_dtypes(include=np.number).columns.to_list()

    # Heatmap to plot the Numeric Features and Rented Bike Count Correlation
    canvas = plt.figure(figsize=(10, 5))
    st.markdown('### Correlation of Rented Bike Count and Weather Condition Features')
    sns.heatmap(data[num_cols_raw].corr(), cmap="Spectral", annot=True) 
    
    st.pyplot(canvas)
    st.markdown('From the heatmap, we can see that every numeric columns in the data has a relatively good correlation with the Rented Bike Count target. There are 6 columns that has a positive correlation and 3 columns with negative correlation. Correlation method used in this heatmap is the pearson r correlation because we want to see the linear relationship of the columns.')

    st.text('Basyira Sabita - 2024')
if __name__=='__main__':
    run()