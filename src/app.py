import streamlit as st
from osmnx_color_roads import generate_image
import pandas as pd
st.title('Color city generator')

# Add a widget to the sidebar to select number of colors:
key_size = st.sidebar.number_input(
    'How many colors?',
    1, 20, 10
)

city = ""
city = st.text_input("city", value='', max_chars=None, key=None, type='default')
st.write('You selected: ', city)

if len(city)>2:
    with st.spinner('Wait for it...'):
        fig, top, popular_words, palette_key  = generate_image(city, query_type='string', key_size=key_size, line_width=0.5)
    st.pyplot()
