import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
place_x = st.selectbox("Select the data for the X-axis",
                       ("GDP", "Happiness", "Generosity"))
place_y = st.selectbox("Select the data for the Y-axis",
                       ("GDP", "Happiness", "Generosity"))
st.subheader(f"{place_x} and {place_y}")

df = pd.read_csv("happy.csv")

place_x = place_x.lower()
place_y = place_y.lower()

figure = px.scatter(df, x=place_x, y=place_y,
                    labels={"x": f"{place_x}",
                            "y": f"{place_y}"})

st.plotly_chart(figure)
