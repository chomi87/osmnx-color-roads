# Streamlit app for osmnx-color-roads
Docker container to deploy a streamlit app to make city maps

# osmnx-color-roads
Quickly generate maps of road networks coloured by words in road names

## What it does

* Runs a streamlit based webapp to interact with the osmnx-color-roads codebase
* The code generates a map with street colored based on the most common words in the OSM. graph of the city

## Installation and usage without docker
TODO

## Installation with docker-compose

* clone the repository
* install docker and coker-compose on your machine
* `cd` in the directory to the level of the docker-compose.yml file
* build and  run the docker image using
```
docker-compose up
```

Note: using docker compose you mount the src folder in the container. This allows for changes in the sourcecode to have
direct effect in the application without rebuilding the container. 

## Installation with docker

* clone the repository
* install docker on your machine
* `cd` in the directory to the level of the Dockerfile
* build the docker image
```
docker build -t <name> -f Dockerfile .
```
* run the docker container
```
docker run -p 8501:8501 <name>
```

## Example usage with docker:
* go to `http://localhost:8501/`
* type the name of a city (adding the country helps)
* ...
* profit

## Inspiration
Extending the work of timfernando
-> https://github.com/timfernando/osmnx-color-roads

Inspiration and original code from Giuseppe Sollazzo @puntofisso
-> https://twitter.com/puntofisso/status/1213135545121099777?s=20

Building on work by Cédric Scherer @CedScherer and @erdavis

