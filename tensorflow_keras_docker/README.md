# Deep Learning - Docker

Use this Dockerfile to build a Deep Learning Conda environment with Python 3, Anconda 3, Tensorflow, Keras, Seaborn, Pandas etc.

## To Build the Docker Image
Pull the Dockerfile to any directory

```
docker image build -t <new_image_name> .
# Example
docker image build -t dltensorflow .
```
Don't forget the dot at the end pointing to the Dockerfile location.

## To Run
```
docker run -i -t -v ${PWD}:/app <new_image_name> /bin/bash
# Example
docker run -i -t -v ${PWD}:src dltensorflow /bin/bash
```
This will also mount the current directory into the working directory in the container.

Once inside the container, do
```
conda activate deeplearning
python
```

# Prebuilt Docker Image
A prebuilt Docker image is also available at Docker Hub. Just do
```
docker pull krexspace/dlconda
```
