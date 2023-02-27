import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

st.title("Dashboard")

FILE_DIR = pd.read_csv(r"C:/Users/manis/OneDrive/Desktop/iris/Iris.csv")



st.dataframe(FILE_DIR)

species = st.selectbox("Select the Species:", FILE_DIR['Species'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(FILE_DIR[FILE_DIR['Species'] == species], x="SepalLengthCm")
col1.plotly_chart(fig_1,use_container_width=True )

fig_2 = px.box(FILE_DIR[FILE_DIR['Species'] == species], y="SepalLengthCm")
col2.plotly_chart(fig_2, use_container_width=True)