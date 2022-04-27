import numpy as np


def gaussian_function(x, x0, a=1, sigma=1, norm=False):

    if norm == True:
        a = 1 / (sigma * np.sqrt(2 * np.pi))

    gauss_exp = -((x - x0) ** 2) / sigma ** 2
    gauss_y = a * np.exp(gauss_exp / 2)

    return gauss_y
