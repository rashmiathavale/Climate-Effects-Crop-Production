import streamlit as st
from constants import STATES, CROPS
import csv
import matplotlib.pyplot as plt

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

x = []
y = []
  
#with open(filename,'r') as csvfile:
    #plots = csv.reader(csvfile)
      
    #for row in plots:
x.append(2017, 2012, 2007, 2002, 1997)
y.append(1)
  
plt.Line2D(x, y)
plt.xlabel('Year')
plt.ylabel('Crop Production')
plt.title('Production of {crops} in {counties} County')
plt.show()
st.write(plt)