import cv2
import streamlit as st
from _datetime import datetime

st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        now = datetime.now()

        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        text = cv2.putText(img=frame, text=now.strftime("%A"), org=(40, 50),
                           fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1.5,
                           color=(255, 255, 255), thickness=2,
                           lineType=cv2.LINE_AA)

        text = cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(50, 70),
                           fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1,
                           color=(255, 0, 0), thickness=2,
                           lineType=cv2.LINE_AA)

        streamlit_image.image(frame)
