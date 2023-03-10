import streamlit as st
import plotly.express as px
import sqlite3
import pandas as pd

conn = sqlite3.connect('date_temperature.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM temperature_date')
rows = cursor.fetchall()

df = pd.DataFrame(rows, columns=['Date', 'Temperature'])

pos_figure = px.line(df, x='Date', y='Temperature',
                     labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(pos_figure)
