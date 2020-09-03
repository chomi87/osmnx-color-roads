import streamlit as st
from osmnx_color_roads import generate_image
import pandas as pd
st.title('Color city generator')
city = st.text_input("city", value='', max_chars=None, key=None, type='default')

st.write('You selected: ', city)

fig, a,b,c  = generate_image(city, query_type='string', key_size=9, line_width=0.5)
st.pyplot()
