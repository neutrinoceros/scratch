# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "matplotlib>=3.3",
#     "scipy>=1.11",
# ]
# ///
"""A simple gaussian isotropic beam class"""
import numpy as np
from scipy.signal import convolve
from scipy.signal.windows import gaussian

class SimpleBeam:
    """A gaussian circular beam model"""
    def __init__(self, pixels_per_beam=None, pixel_size=None, beam_size=None):
        if pixels_per_beam is None and (pixel_size is None or beam_size is None):
            raise ValueError
        if pixels_per_beam is not None:
            self.pixels_per_beam = float(pixels_per_beam)
        else:
            self.pixels_per_beam = beam_size / pixel_size
        if self.pixels_per_beam == 0.:
            raise ValueError(beam_size)

    def _get_kernel(self, nx, ny):
        kernel = np.outer(gaussian(M=nx, std=self.pixels_per_beam),
                          gaussian(M=ny, std=self.pixels_per_beam))
        return kernel

    def apply(self, img: np.ndarray) -> np.ndarray:
        kernel = self._get_kernel(*img.shape)
        return convolve(img.data, kernel, mode="same")


if __name__ == "__main__":
    """Minimal demo"""
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle

    fig, axes = plt.subplots(ncols=3, nrows=3, figsize=(14, 14), sharex=True, sharey=True)

    ppbs = np.arange(1, 21, 4)
    for nline, struct_size in enumerate([5, 10, 100]):
        # fakedata
        raw_data = np.ones(10000).reshape(100, 100)
        for i in range(50):
            raw_data[-i-1] *= 2 + np.sin(2*i*np.pi/struct_size)
            raw_data[i] = 0

        for j in range(100):
            raw_data[:, j] *= j

        axes[nline, 0].imshow(raw_data)
        for ppb, ax in zip(ppbs, axes[nline, 1:]):
            mybeam = SimpleBeam(pixels_per_beam=ppb)
            ax.imshow(mybeam.apply(raw_data))
            ax.add_patch(Circle(xy=(10, 10), radius=mybeam.pixels_per_beam, facecolor="white"))
        plt.savefig("beam_demo_output.png")
