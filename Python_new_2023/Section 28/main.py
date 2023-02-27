import streamlit as st
import requests

api_key = "NBuB0dETz4K64tF1C6XHOtodDVGCjMul7AJLpqAu"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

request = requests.get(url)
content = request.json()

st.title(content["title"])
st.image(content["hdurl"])
st.text_area(content["explanation"])
