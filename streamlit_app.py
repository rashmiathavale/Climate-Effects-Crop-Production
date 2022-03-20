import streamlit as st
from constants import STATES, CROPS
import csv
import pandas as pd
import altair as alt

st.title("Climate Effects on Crop Production")

filename = 'Crops.csv'
COUNTIES = []

col1, col2, col3 = st.columns(3)

with col1:
    states = st.selectbox("Select a state", STATES).strip()

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if row[1] == states:
            COUNTIES.append(row[0]);

with col2:
    counties = st.selectbox("Select a county", COUNTIES).strip()

with col3:
    crops = st.selectbox("Select a state", CROPS).strip()

chart_data = pd.DataFrame({
    'pig': [20, 18, 489, 675, 1776],
    'horse': [4, 25, 281, 600, 1900]}, 
    index=[2017, 2012, 2007, 2002, 1997])

line_chart = alt.Chart(chart_data).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
).properties(
    title='Sales of consumer goods'
)

st.altair_chart(line_chart)