import streamlit as st
import requests
import numpy as np

st.set_page_config(page_title="Hello", page_icon="🔥")

st.markdown("# Streamlit is awesome! :rocket:")

if st.button("Click"):
    st.image("../raw_data/Icon_Red.png", width=200)

query = st.text_input("Search a gif")

url = "https://api.giphy.com/v1/gifs/search"
params={"api_key": st.secrets.api_key, "q": query}

response = requests.get(url, params=params).json()

while not query:
    st.stop()

gif_url = response["data"][np.random.randint(0,10)]["embed_url"]

st.markdown(
    f'<iframe src="{gif_url}" width="500" height="300"></iframe>',
    unsafe_allow_html=True
)
