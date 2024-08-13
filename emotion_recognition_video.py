import os
import streamlit as st
from deepface import DeepFace
from PIL import Image
import time
import cv2


st.title("Facial Verification")
st.write("\n")
st.write("\n")
st.subheader("Verify if facial images are similar")
st.write("\n")
st.write("\n")
file_upload_1 = st.file_uploader("Upload your first facial image", type=['mp4'], key='img_1')
st.write("\n")

style = "<style>.row-widget.stButton {text-align: center;}</style>"
st.markdown(style, unsafe_allow_html=True)


if st.button("Analyze"):
    results_dict = {}
    if file_upload_1 is not None:
        video = cv2.VideoCapture(file_upload_1)
        while True:
            ret, frame = video.read()
            if ret:
                st.image(frame)
                result = DeepFace.analyze(
                    img_path=frame,
                    actions=['age', 'gender', 'race', 'emotion'],
                )
                results_dict[frame] = result
                if st.button("Stop"):
                    break
                else:
                    break
        video.release()

        st.dataframe(results_dict)