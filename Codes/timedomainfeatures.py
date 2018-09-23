# Time Domain Features
# Energy of the most significant peaks i.e. first 3-4 peaks
# Mean and Standard Deviation of the peaks
# Time between each peaks

import numpy as np
from scipy.signal import find_peaks_cwt


def find_peaks(filtered_signal, signal_index):

    indexes = find_peaks_cwt(filtered_signal, np.arange(1, 550), min_length=50)

    if indexes.size != 0:
        print(signal_index)
        print(indexes[0:2])
