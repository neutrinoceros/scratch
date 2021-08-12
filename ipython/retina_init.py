# install:
# copy this file to ~/.ipython/profile_default/startup/
from importlib.util import find_spec
if find_spec("matplotlib") and find_spec("matplotlib_inline"):
    from matplotlib_inline import backend_inline
    backend_inline.set_matplotlib_formats("retina")
