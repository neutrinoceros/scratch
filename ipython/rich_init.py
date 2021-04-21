# install:
# copy this file to ~/.ipython/profile_default/startup/
def rich_init():
    """
    Doing this in a function keeps pollution into the global
    namespace at a minimal level.
    Credits to Waylon Walker for this remark. 
    """
    from rich import pretty, traceback
    pretty.install()
    traceback.install()

if __name__ == "__main__":
    try:
        rich_init()
    except ImportError:
        pass
