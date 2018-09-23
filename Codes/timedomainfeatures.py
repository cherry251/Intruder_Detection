# Time Domain Features
# Energy of the most significant peaks i.e. first 3-4 peaks
# Mean and Standard Deviation of the peaks
# Time between each peaks

import numpy as np
from myfunctions import peak_detector


def find_peaks(filtered_signal):

    t = range(188)
    max, min = peak_detector(filtered_signal, 0.0, 0.0005, t)  # Calculating the peaks
    xmax = np.zeros(len(max))  # Maximum indexes
    ymax = np.zeros(len(max))  # Maximum values
    xmin = np.zeros(len(min))  # Minimum indexes
    ymin = np.zeros(len(min))  # Minimum values

    for i in range(len(max)):
        np.put(xmax, i, max[i][0])
        np.put(ymax, i, max[i][1])

    for j in range(len(min)):
        np.put(xmin, j, min[j][0])
        np.put(ymin, j, min[j][1])

    xmax = [ele*0.02 for ele in xmax]  # Adjusting to time series
    xmin = [ele*0.02 for ele in xmin]  # Adjusting to time series

    return xmax, ymax, xmin, ymin


