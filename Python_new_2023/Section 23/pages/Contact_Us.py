import streamlit as st
import pandas as pd
from send_email import send_email

df = pd.read_csv("topics.csv")

st.header("Contact Me")

with st.form(key="emails_form"):
    user_email = st.text_input("Enter Email Address")
    topic = st.selectbox("What topic would you like to discuss", df["topic"])
    row_message = st.text_area("Text")
    message = f"""\
Subject: Email from {user_email}

From: {user_email}
Topic {topic}
{row_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
