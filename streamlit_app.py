import streamlit as st
from constants import STATES, CROPS
import csv
import pandas as pd
import altair as alt

st.title("Climate Effects on Crop Production")

filename = 'Crops.csv'
COUNTIES = []
county = ""
crop = ""

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
    county = counties

with col3:
    crops = st.selectbox("Select a state", CROPS).strip()
    crop = crops

chart_data = pd.DataFrame({
    'year': [1997, 2002, 2007, 2012, 2017], 'crop-production': [12, 30, 50, 100, 234]})

chart = (
        alt.Chart(
            data=chart_data,
            title="Production of {0} in {1} County".format(crop, county),
        )
        .mark_line()
        .encode(
            x = alt.X("year", axis=alt.Axis(title="Year")),
            y = alt.Y("crop-production", axis=alt.Axis(title="Crop Production")),
        )
)

st.altair_chart(chart)