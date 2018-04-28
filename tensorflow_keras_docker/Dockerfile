FROM continuumio/anaconda3
# ENV LAST_UPDATED 20180427
ARG conda_env=deeplearning

# Update conda itself
RUN conda update -y conda

# Create the conda environment
RUN conda create -y -n ${conda_env} python

# Install dependencies
RUN conda install -y -n ${conda_env} ipython
RUN conda install -y -n ${conda_env} jupyter
RUN conda install -y -n ${conda_env} pandas
RUN conda install -y -n ${conda_env} seaborn
RUN conda install -y -n ${conda_env} scipy
RUN conda install -y -n ${conda_env} scikit-learn

# Install Tensorflow and keras through pip
RUN /opt/conda/envs/${conda_env}/bin/pip install --upgrade pip
RUN /opt/conda/envs/${conda_env}/bin/pip install --upgrade tensorflow
RUN /opt/conda/envs/${conda_env}/bin/pip install --upgrade keras

# Change working directory
WORKDIR /app

CMD /bin/bash
