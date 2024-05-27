import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache_data
def load_csv():
    data = pd.read_csv('raindata.csv')
    return data



def plot_rainfall(city, year, data):
    city_data = data[(data['City'] == city) & (data['Year'] == year)]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(city_data.columns[2:],city_data.iloc[0,2:], marker='o', linestyle='-', color='g')

    ax.set_title(f'Rainfall Data for {city} in {year}')
    ax.set_xlabel('Year')
    ax.set_ylabel('Rainfall (mm)')

    st.pyplot(fig)





def main_func():

    st.title("Rainfall Data Visualization")

    data = load_csv()

    st.write('### Data Preview')
    st.dataframe(data.head())

    cities = data['City'].unique()
    years = data['Year'].unique()

    # Create dropdown for year selection
    year = st.selectbox("Select a year:", years)


    # Plot the rainfall data for the selected city when a button is clicked
    st.write("### Select a city to view its rainfall data:")

    for city in cities:
        if st.button(city):
            plot_rainfall(city, year, data)


main_func()
