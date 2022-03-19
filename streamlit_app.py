from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from constants import STATES

st.title("Climate Effects on Crop Production")

states = st.selectbox("Select a state", STATES).strip()
