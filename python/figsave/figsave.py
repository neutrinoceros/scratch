"""A reusable class to save figures with multiple configs in one line"""
import json
import os
from os.path import expandvars
from pathlib import Path


class FigSaver:
    def __init__(self, conf: dict, save_kwargs: dict = None):

        if isinstance(conf, (str, os.PathLike)):
            if not Path(conf).suffix == ".json":
                raise TypeError("input conf file needs to be json")
            with open(conf, mode="rt") as fp:
                conf = json.load(fp)
        elif isinstance(conf, dict):
            pass
        else:
            raise TypeError("conf needs to be a Path, str or dict")

        self.save_kwargs = save_kwargs or {}
        self.specs = conf["specs"]

        self.savedir = Path(expandvars(conf["savedir"]))
        if not self.savedir.is_dir():
            # os.mkdir() will not create directories recursively
            # so an error is raised if more than one level is missing (this is intented)
            os.mkdir(self.savedir)

        
    def save(self, figure, stem:str, verbose=False, **top_kwargs):
        for dirname, kwargs in self.specs.items():
            out = self.savedir / dirname
            if not out.is_dir():
                os.makedirs(out)
            try:
                savepath = out/f"{stem}.{kwargs['format']}"
                figure.savefig(savepath,
                               bbox_inches="tight",
                               **kwargs, **self.save_kwargs)
                if verbose: print(f"saved to {savepath}")
            except ValueError:
                print(f"Warning: failed saving to {kwargs['format']}")


# test area
if __name__ == "__main__":
    import matplotlib.pyplot as plt

    conf = {
        "savedir": "output",
        "specs":
        {
            "pdf": dict(format="pdf"),
            "png": dict(format="png"),
            "hd": dict(format="jpg", dpi=500)
        }
    }
    import json
    with open("testconf.json", mode="wt") as fp:
        json.dump(conf, fp)
    
    with open("testconf.json", mode="rt") as fp:
        conf2 = json.load(fp)
    
    fs = FigSaver(conf2)
    fig, axes = plt.subplots()
    fs.save(fig, "empty_test_fig")
