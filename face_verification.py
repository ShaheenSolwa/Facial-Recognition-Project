import os
import streamlit as st
from deepface import DeepFace
from PIL import Image

st.title("Facial Verification")
st.write("\n")
st.write("\n")
st.subheader("Verify if facial images are similar")
st.write("\n")
st.write("\n")
file_upload_1 = st.file_uploader("Upload your first facial image", type=["png", "jpg", "jpeg"], key='img_1')
st.write("\n")
file_upload_2 = st.file_uploader("Upload your second facial image", type=["png", "jpg", "jpeg"], key='img_2')
st.write("\n")
st.write("\n")

col1, col2 = st.columns(2)

if file_upload_1 and file_upload_2:
    style = "<style>.row-widget.stButton {text-align: center;}</style>"
    st.markdown(style, unsafe_allow_html=True)

    img_path_1 = "img_1.jpg"
    img_path_2 = "img_2.jpg"
    with open(img_path_1, "wb") as f:
        f.write(file_upload_1.getbuffer())
    with open(img_path_2, "wb") as f:
        f.write(file_upload_2.getbuffer())

    col1, col2 = st.columns(2)
    col1.subheader("Image 1")
    col1.image(Image.open(img_path_1))
    col2.subheader("Image 2")
    col2.image(Image.open(img_path_2))

    st.write("\n")
    st.write("\n")

    if st.button("Verify"):
        result = DeepFace.verify(
            img1_path=img_path_1,
            img2_path=img_path_2
        )

        st.dataframe(result)

    # Delete the temporary files
    os.remove(img_path_1)
    os.remove(img_path_2)