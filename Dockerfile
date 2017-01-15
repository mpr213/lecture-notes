FROM andrewosh/binder-base

MAINTAINER Logan G. Page <logan.page@up.ac.za>

### Python2 ###
# Install from requirements
RUN pip install -r requirements.txt

# Install and enable extensions
RUN jupyter-nbextension install --sys-prefix --py nbtutor
RUN jupyter-nbextension enable --sys-prefix --py nbtutor

### Python3 ###
# Install from requirements
RUN /home/main/anaconda2/envs/python3/bin/pip install -r requirements.txt

# Install and enable extensions
RUN /home/main/anaconda2/envs/python3/bin/jupyter-nbextension install --sys-prefix --py nbtutor
RUN /home/main/anaconda2/envs/python3/bin/jupyter-nbextension enable --sys-prefix --py nbtutor

# Install notebook config
ADD jupyter_notebook_config.py /home/main/.jupyter/jupyter_notebook_config.py
