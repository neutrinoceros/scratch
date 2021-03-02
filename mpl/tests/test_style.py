from pathlib import Path

import numpy as np
import pytest

import matplotlib as mpl
import matplotlib.pyplot as plt


# defs
xlims = (1e-6, 3 * np.pi)
x1 = np.linspace(*xlims, 100)
x2 = np.geomspace(*xlims, 100)


def setup_plot(ax):
    ax.plot(x1, np.sin(x1) / x1)

    ax.plot(x2, -np.sin(x2) / x2, marker="x")

    ax.plot(x1, np.exp(-(x1 ** 2) / 4), lw=0, marker="+")
    ax.plot(x2, -np.exp(-(x2 ** 2) / 4), lw=0, marker="v")

    ax.plot(x1, 1 / np.exp(x1), lw=2, ls="--")
    ax.plot(x2, -1 / np.exp(x2), lw=2, ls="-.")

    ax.annotate(text="An annotation", xy=(4, 0.4))
    ax.set_xlabel(r"$r$ [cm]")
    ax.set_ylabel(r"$I$ [W.cm$^{-2}$]")


STYLESHEET = Path.joinpath(Path(__file__).parents[1], "style", "main.mplstyle")
mpl_compare = pytest.mark.mpl_image_compare(
    style=STYLESHEET,
    savefig_kwargs={"bbox_inches": "tight"},
)

@mpl_compare
def test_colorcycle():
    fig, ax = plt.subplots()
    x = np.arange(10)
    for i in range(11):
        ax.plot(x, i + x, lw=13)
    return fig

@mpl_compare
def test_singlepanel():
    fig, ax = plt.subplots()
    setup_plot(ax)
    return fig


@mpl_compare
def test_2by2():
    fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
    for ax in axes.flat:
        setup_plot(ax)
    return fig


@mpl_compare
@pytest.mark.parametrize("context", ["notebook", "poster", "talk", "paper"])
def test_seaborn_context(context):
    import seaborn as sns

    sns.set_context(context)
    fig, ax = plt.subplots()
    setup_plot(ax)
    sns.reset_orig()
    return fig
