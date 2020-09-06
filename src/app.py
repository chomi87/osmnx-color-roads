import streamlit as st
import osmnx as ox
from osmnx_color_roads import generate_image, palette_generator, color_for_road, find_common_words, get_data_point, get_data, normalise_str, create_legend_lines
import pandas as pd

#config
line_width = 1
dpi = 300
place=""
which_result = 1
network_type = "all"
word_list = None

#display title and intro text
st.title('Color city generator - LIVE!')
st.subheader('Generate a map of a city with roads colored by their type (road, street, ...)')

# Add a widget to the sidebar to select number of colors:
key_size = st.sidebar.number_input(
    'How many colors?',
    1, 20, 10
)
# Add a widget to the sidebar to enter a list of keywords:
word_input = st.sidebar.text_input("Comma separated list of keywords - leave blank to auto-detect",
                                   value="", max_chars=None, key=None, type='default')


#if there was an input, parse it
if len(word_input)>2:
    word_list = word_input.split(",")
    word_list = [normalise_str(word) for word in word_list]

#widget to enter the city
place = st.text_input("City, Country", value='', max_chars=None, key=None, type='default')
st.write('You selected: ', place)

#if a city was entered, enter the main cycle
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
        lines = create_legend_lines(palette_key)
        ax.set_title(place, {'fontsize': 22})
        ax.legend(lines,palette_key.keys(), fontsize="x-large", frameon=False, mode="expand")

        st.pyplot()

    #output the top words and counts
    sorted_dict = sorted(popular_words.items(), key=lambda item: item[1], reverse=True)
    df = pd.DataFrame(sorted_dict)
    st.sidebar.write(df)