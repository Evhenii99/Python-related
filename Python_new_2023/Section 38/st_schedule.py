import streamlit as st
import plotly.express as px
import pandas as pd

content = pd.read_csv("data.txt")

pos_figure = px.line(content, x='date', y=' temperature',
                     labels={"x": "Date", "y": "Temperature (C)"})

st.plotly_chart(pos_figure)
