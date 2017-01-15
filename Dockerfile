FROM andrewosh/binder-base

MAINTAINER Logan G. Page <logan.page@up.ac.za>

# Update form requirements
RUN pip install -r requirements.txt

# Install and enable extensions
RUN pip install git+git://github.com/lgpage/nbtutor.git
RUN jupyter nbextension install --sys-prefix --py nbtutor
RUN jupyter nbextension enable --sys-prefix --py nbtutor

# Install notebook config
ADD jupyter_notebook_config.py /home/main/.jupyter/jupyter_notebook_config.py
