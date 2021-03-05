import labtables as lab
import numpy as np
import matplotlib.pyplot as plt

paths = (
   'item_10_1_coarse.csv',
   'item_10_1_fine.csv',
   'item_10_6_coarse.csv',
   'item_10_6_fine.csv',
)

for path in paths:
    freq, time_diff = map(np.array, lab.read_csv(path))
    freq *= 1e3  # convert from kHz to Hz
    time_diff *= 1e-6  # convert from us to seconds
    #phase_diff = 2 * np.pi * time_diff / (1 / freq)
    phase_diff = 2 * np.pi * time_diff / (1 / freq)

    plt.close()
    plt.scatter(freq, phase_diff)
    plt.xlabel('Частота, кГц')
    plt.ylabel('Разность фаз, рад')
    plt.grid()
    plt.savefig(path[:-4] + '.png')
