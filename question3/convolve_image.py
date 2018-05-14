import numpy as np
import scipy
from scipy.signal import fftconvolve
import matplotlib.pyplot as plt

from plot_questions import point_spread_img_vals

def convolve_img(fname):
    img = scipy.misc.imread(fname)
    #print img.shape

    plt.figure()
    kernel = point_spread_img_vals()
    #print kernel.shape
    kernel_3channels = np.repeat(kernel[:, :, np.newaxis], 3, axis=2) # Convert to 3 channels
    #print kernel_3channels.shape

    convolved_img = fftconvolve(img, kernel_3channels, mode="same")
    #print convolved_img.shape
    plt.imshow(convolved_img)
    plt.show()

if __name__ == "__main__":
    convolve_img("proxima_centauri.jpg")
