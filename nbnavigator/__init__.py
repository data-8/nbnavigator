from nbnavigator.handlers import setup_handlers
# Jupyter Extension points
def _jupyter_server_extension_paths():
    return [{
        'module': 'nbnavigator',
    }]

def _jupyter_nbextension_paths():
    return [{
        "section": "tree",
        "dest": "nbnavigator",
        "src": "static",
        "require": "nbnavigator/main"
    }]

def load_jupyter_server_extension(nbapp):
    setup_handlers(nbapp)
