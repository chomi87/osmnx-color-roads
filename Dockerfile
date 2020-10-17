# Python 3.6
FROM continuumio/miniconda3
MAINTAINER Michael Chong
RUN conda config --prepend channels conda-forge

#RUN conda create -n env python=3.6
RUN conda create -n ox --strict-channel-priority osmnx python=3.6

RUN echo "source activate ox" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "ox", "/bin/bash", "-c"]

# Make sure the environment is activated:
RUN echo "Make sure osmnx is installed:"
RUN python -c "import osmnx"

# Create work dir, and copy all files
WORKDIR /app/

RUN conda install pip
RUN pip install streamlit
RUN pip install seaborn
RUN pip install stop-words

# Make sure the environment is activated:
RUN echo "Make sure streamlit is installed:"
RUN python -c "import streamlit"

# Maintain structure with src
# Create directories
RUN mkdir -p src/

# Copy only relevant data
COPY src/ /app/src/

# Expose port
EXPOSE 8501

# Set python env
ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PYTHONPATH "${PYTHONPATH}:/app/src"
ENV PATH="$HOME/.local/bin:$PATH"

# start app
CMD streamlit run /app/src/app.py
