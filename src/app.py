import streamlit as st
import osmnx as ox
from osmnx_color_roads import generate_image, palette_generator, color_for_road, find_common_words, get_data_point, get_data, normalise_str
import pandas as pd

#config
line_width = 1
dpi = 300
key_size = 10
place=""
which_result = 1
network_type = "all"
word_input = ""
word_list = None

st.title('Color city generator')
st.subheader('Generate a map of a city with roads colored by their type (road, street, ...)')

# Add a widget to the sidebar to select number of colors:
key_size = st.sidebar.number_input(
    'How many colors?',
    1, 20, 10
)

word_input = st.sidebar.text_input("Comma separated list of words to use - leave blank to auto-detect",
                                   value="", max_chars=None, key=None, type='default')

if len(word_input)>2:
    word_list = word_input.split(",")
    word_list = [normalise_str(word) for word in word_list]

place = st.text_input("city", value='', max_chars=None, key=None, type='default')
st.write('You selected: ', place)

if len(place)>2:
    with st.spinner('Fetching graph...'):
        graph = get_data(place, which_result = which_result, network_type = network_type)

    with st.spinner('Get the metadata from the graph edges...'):
        edge_attributes = ox.graph_to_gdfs(graph, nodes=False)
        edge_attributes.loc[:, "name"] = edge_attributes.loc[:, "name"].fillna("").map(normalise_str)

    with st.spinner('Find the most popular words in the names...'):
        # Find the most popular words in the names,
        # these should be things like 'road', 'street' etc
        popular_words = find_common_words(edge_attributes, word_list)
        top = dict(list(popular_words.items())[0: key_size])

    with st.spinner('Generating color palette...'):
        palette_key = palette_generator(top)

    with st.spinner('Applying palette...'):
        edge_colors = [color_for_road(row['name'], palette_key)
                       for _, row in edge_attributes.iterrows()]

    with st.spinner('Drawing the plot...'):
        # Draw the plot
        fig, ax = ox.plot_graph(graph, bgcolor='white', node_size=0,
                                node_color='w', node_edgecolor='gray',
                                node_zorder=2, edge_color=edge_colors,
                                edge_linewidth=line_width, edge_alpha=0.98,
                                figsize=(20, 20), dpi=dpi, save=False,
                                )

    sorted_dict = sorted(popular_words.items(), key=lambda item: item[1], reverse=True)
    df = pd.DataFrame(sorted_dict, columns=["Word", "Count"]).head(2*key_size)

    st.pyplot()
    st.sidebar.write(df)


