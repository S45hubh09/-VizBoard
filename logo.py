import streamlit as st
from PIL import Image

# Load and display the logo from the 'assets' folder
logo = Image.open("assets/logo.jpg")  # or logo.png
st.image(logo, width=145)
