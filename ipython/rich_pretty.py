# install:
# copy this file to ~/.ipython/profile_default/startup/
try:
    from rich import pretty
    pretty.install()
except ImportError:
    pass
