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

colCounter = 0
first = 0
second = 0
third = 0
fourth = 0
fifth = 0

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

chart1 = (
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

temp_data = pd.DataFrame({
    'year': ['1997', '2002', '2007', '2012', '2017'], 'temperature': [23,43,65,78,87]})

chart2 = (
        alt.Chart(
            data=temp_data,
            title="Temperature in {0} County".format(county),
        )
        .mark_line()
        .encode(
            x = alt.X("year", axis=alt.Axis(title="Year")),
            y = alt.Y("temperature", axis=alt.Axis(title="Temperature")),
        )
)

col1, col2 = st.columns(2)

col1, col2 = st.columns(2)

with col1:
    st.altair_chart(chart1)
with col2:
    st.altair_chart(chart2)

# https://remarkablemark.org/blog/2020/08/26/python-iterate-csv-rows/