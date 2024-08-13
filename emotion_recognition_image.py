import os
import streamlit as st
from deepface import DeepFace
from PIL import Image
import time


st.title("Facial Verification")
st.write("\n")
st.write("\n")
st.subheader("Verify if facial images are similar")
st.write("\n")
st.write("\n")
file_upload_1 = st.file_uploader("Upload your first facial image", type=["png", "jpg", "jpeg"], key='img_1')
st.write("\n")

style = "<style>.row-widget.stButton {text-align: center;}</style>"
st.markdown(style, unsafe_allow_html=True)

if st.button("Analyze"):

    Image.open(file_upload_1).save(f'analyzed_image.{file_upload_1.name.split(".")[-1]}')

    objs = DeepFace.analyze(
      img_path = f'analyzed_image.{file_upload_1.name.split(".")[-1]}',
      actions = ['age', 'gender', 'race', 'emotion'],
    )

    st.write(objs)

    time.sleep(1)

    os.remove(f'analyzed_image.{file_upload_1.name.split(".")[-1]}')