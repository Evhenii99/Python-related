import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


st.header("Apple")
st.write("""
Apple Inc. (formerly Apple Computer Inc.) is an American computer and consumer electronics company famous
 for creating the iPhone, iPad and Macintosh computers. Apple is one of the largest companies globally with 
 a market cap of over 2 trillion dollars.

Apple devices are renowned for their design aesthetic and attention to detail. 
Tight integration between hardware and software gives their systems a performance 
advantage over competitor systems with similar specifications.
""")
st.subheader("Our team")

col1, col2, col3 = st.columns([1, 1, 1])

df = pd.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name']}".title())
        st.write(row["role"])
        st.image("images/" + row["image"])


with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name']}".title())
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name']}".title())
        st.write(row["role"])
        st.image("images/" + row["image"])
