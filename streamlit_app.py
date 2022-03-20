import streamlit as st
from constants import STATES, CROPS
import csv
import pandas as pd
import altair as alt

st.title("Climate Effects on Crop Production")

filename = 'Crops-2017.csv'
COUNTIES = []
county = ""
crop = ""
state = ""

col1, col2, col3 = st.columns(3)

with col1:
    states = st.selectbox("Select a state", STATES).strip()
    state = states

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

first, second, third, fourth, fifth = 0
colCounter = 0

with open('Crops-2017.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        for i in range(2, 6):
            if (row[i] == crop):
                colCounter = i;
        for col in datareader:
            if (col[0] == county and col[1] == state):
                first = col[colCounter]
        

with open('Crops-2012.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        for i in range(2, 6):
            if (row[i] == crop):
                colCounter = i;
        for col in datareader:
            if (col[0] == county and col[1] == state):
                second = col[colCounter]

with open('Crops-2007.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        for i in range(2, 6):
            if (row[i] == crop):
                colCounter = i;
        for col in datareader:
            if (col[0] == county and col[1] == state):
                third = col[colCounter]

with open('Crops-2002.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        for i in range(2, 6):
            if (row[i] == crop):
                colCounter = i;
        for col in datareader:
            if (col[0] == county and col[1] == state):
                fourth = col[colCounter]

with open('Crops-1997.csv', 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        for i in range(2, 6):
            if (row[i] == crop):
                colCounter = i;
        for col in datareader:
            if (col[0] == county and col[1] == state):
                fifth = col[colCounter]

chart_data = pd.DataFrame({
    'year': ['1997', '2002', '2007', '2012', '2017'], 'crop-production': [first, second, third, fourth, fifth]})

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