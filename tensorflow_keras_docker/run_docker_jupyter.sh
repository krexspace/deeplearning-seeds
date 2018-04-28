# Runs the Jupyter docker in the deeplearning conda environment at port 8888
sudo docker run -i -t -p 8888:8888 krexspace/dlconda /bin/bash -c "/opt/conda/envs/deeplearning/bin/jupyter notebook --notebook-dir=/app --ip='*' --port=8888 --no-browser --allow-root"

