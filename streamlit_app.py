from collections import namedtuple
import altair as alt
import pandas as pd
import streamlit as st
from constants import STATES
import matplotlib.pyplot as plt
import csv

filename = 'Crops.csv'

st.title("Climate Effects on Crop Production")

states = st.selectbox("Select a state", STATES).strip()
COUNTIES = [];

with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        if row[1] == states:
            COUNTIES += row[0];

counties = st.selectbox("Select a county", COUNTIES).strip()
