import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
st.set_page_config(layout="wide") # call page_config directly after the imports.

st.title('Visualize Booking Data')


@st.cache
def get_Data(nrows):
    try:
        df = pd.read_excel("data/Input Reservationsdaten.xlsx", nrows=nrows)
        df['Created at (lead time to start date)'] = pd.to_datetime(df['Created at (lead time to start date)'])
        df['Created at (lead time to start date)'] = df['Created at (lead time to start date)'].dt.date
        df = df.sort_values(by='Created at (lead time to start date)')
        return df
    except Exception as e:
        print(e)
        print("Error: Could not read data")

# Importing data
data_load_state = st.text('Loading data...')
rows = st.text_input('How many rows you want to show? (Automatically sorted by date)', '10')
st.write("Number of data you've chosen: ", rows)
df = get_Data(int(rows))
data_load_state.text('Loading data...done!')
# Importing data

# Displaying raw data
st.subheader('Raw data')
st.write(df)
# Displaying raw data
############################################################
# Filter by platform options
st.subheader('Filtering by Platform')
platformOptions =  df['Platform'].unique()

setPlatformOptions = set(platformOptions)

option = st.sidebar.selectbox(
'Choose a platform please:',
setPlatformOptions)
st.write('You selected:', option)

st.write(df[df['Platform'] == option])
# Filter by platform options 
############################################################
# Filter by property options
st.subheader('Filtering by Property')
platformOptions =  df['Property'].unique()

setPlatformOptions = set(platformOptions)

option = st.sidebar.selectbox(
'Choose a property please:',
setPlatformOptions)
st.write('You selected:', option)

st.write(df[df['Property'] == option])
# Filter by platform options 
############################################################
# Selecting a date range filtering 
st.subheader('Filtering by Date')

min_date = datetime(2022,1,1)
max_date = datetime(2022,9,1)

st.write('Select first and last date (first date should be earlier than the last date)')
first_date = st.sidebar.date_input("Pick first date",min_value=min_date, max_value=max_date) # 
st.write("You selected as first date:", first_date)

second_date = st.sidebar.date_input("Pick second date",min_value=min_date, max_value=max_date) # 
st.write("You selected as second date:", second_date)

st.write(df[(df['Created at (lead time to start date)']>first_date) & (df['Created at (lead time to start date)']< second_date)])
# Selecting a date range filtering
############################################################
# Selecting a date range using slider
st.write('Select first and last date using slider')
sliderDate = st.sidebar.slider("Pick first date", value=(min_date, max_date), format="YY/MM/DD") #

first_date_slider = sliderDate[0]
second_date_slider = sliderDate[1]

st.write("You selected as first date by using slider:", first_date_slider)
st.write("You selected as second date by using slider:", second_date_slider)

st.write(df[(df['Created at (lead time to start date)']>first_date_slider) & (df['Created at (lead time to start date)']< second_date_slider)])
# Selecting a date range using slider
############################################################