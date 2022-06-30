import streamlit as st
import instaloader
from PIL import Image

image = Image.open('image.png')

col1, col2 = st.solumn(2)

col1.header("Instragram Profile Picture Downloader")
col2.image(image)

try:
   bot1 = instaloader.Instaloader()

   username = st.text_input("Enter Profile Username")

   st.write(bot1.download_profile(username, profile_pic_only=True))
except:
  pass
