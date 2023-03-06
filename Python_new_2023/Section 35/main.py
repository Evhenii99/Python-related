import streamlit as st
import plotly.express as px
from functions import positive_negative, date

pos_value, neg_value = positive_negative()
date = date()


st.title("Diary Tone")

st.subheader("Positivity")
pos_figure = px.line(x=date, y=pos_value, labels={"x": "Date",
                                                  "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(x=date, y=neg_value, labels={"x": "Date",
                                                  "y": "Negativity"})
st.plotly_chart(neg_figure)
