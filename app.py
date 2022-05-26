import streamlit as st
import instaloader

bot1 = instaloader.Instaloader()

username = st.text_input("Enter Profile Username")

st.write(bot1.download_profile(username,profile_pic_only=True))
