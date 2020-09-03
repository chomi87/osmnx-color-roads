# Streamlit app for osmnx-color-roads
Docker container to deploy a streamlit app to make city maps

# osmnx-color-roads
Quickly generate maps of road networks coloured by words in road names

## What it does

* Runs a streamlit based webapp to interact with the osmnx-color-roads codebase
* The code generates a map with street colored based on the most common words in the OSM. graph of the city

## Installation

* clone the repository
* install docker on your machine
* `cd` in the directory
* build the docker image
```
docker build -t <name> -f Dockerfile .
```
* run the docker container
```
docker run -p 8501:8501 <name>
```

## Example usage:
```
from  osmnx_color_roads import generate_image

generate_image('Oahu, Mililani, Honolulu County, Hawaii, United States of America', query_type='string', key_size=9, line_width=0.5)
```

## Inspiration
Extending the work of timfernando
-> https://github.com/timfernando/osmnx-color-roads

Inspiration and original code from Giuseppe Sollazzo @puntofisso
-> https://twitter.com/puntofisso/status/1213135545121099777?s=20

Building on work by Cédric Scherer @CedScherer and @erdavis

#docker #mapgeek #gis #osmnx #opensource #visualization #python #mapvisualization

