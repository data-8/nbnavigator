# nbnavigator
DSEP Infrastructure extension for assignment navigation and fetching assignments. (Based off nbgrader [https://github.com/jupyter/nbgrader], for integration with okPy and datahub.berkeley.edu.

Requirements : Google Oauthenticator with OKpy support. 

Directions:

    git clone https://github.com/data-8/nbnavigator.git
    pip install -e nbnavigator

    jupyter nbextension install --py nbnavigator --sys-prefix
    jupyter nbextension enable nbnavigator --py --sys-prefix

    jupyter serverextension install --py nbnavigator --sys-prefix
    jupyter serverextension enable nbnavigator --py --sys-prefix