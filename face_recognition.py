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
database = st.text_input("Enter the database path")
st.write("\n")
st.write("\n")
if database != '':
    image_files = [os.path.join(database, f) for f in os.listdir(database)]

    # Create two columns
    col1, col2 = st.columns(2)

    # Display the left image
    col1.image(file_upload_1, width=150)

    # Display different images on the right with a time delay
    for image_file in image_files:
        right_image = Image.open(image_file)
        col2.image(right_image, width=150)
        result = DeepFace.find(
            img_path = file_upload_1,
            db_path = image_file
        )
        st.write(result)
        time.sleep(5)