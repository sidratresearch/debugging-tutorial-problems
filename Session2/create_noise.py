# In this script, we create a bunch of noisy data

import numpy as np


def make_data_noisy(tmp1, sigma=1.0):
    n_elements = tmp1.size
    noise = sigma * np.random.randn(n_elements)
    new_data_version = tmp1 + noise

    return new_data_version


x = np.linspace(0, 100, 200)


n_noiselevels = 50
noise_values = np.linspace(-50, 50, 51)

noise_matrix = np.zeros((x.size, n_noiselevels))

for i in range(n_noiselevels):
    y = make_data_noisy(x, sigma=noise_values[i])
    noise_matrix[:, i] = y / np.abs(noise_values[i])

