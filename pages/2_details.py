import streamlit as st
from PIL import Image



img = Image.open('python.jpg')
st.image(img,caption='Python programming')