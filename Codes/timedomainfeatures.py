# Time Domain Features
# Energy of the most significant peaks i.e. maximum and minimum peaks
# Mean and Standard Deviation of the peaks
# Average time between each peaks i.e. average time for stride

import numpy as np
from myfunctions import peak_detector


def find_peaks(filtered_signal):

    t = range(400)
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

    xmax = [ele*0.01 for ele in xmax]  # Adjusting to time series
    xmin = [ele*0.01 for ele in xmin]  # Adjusting to time series

    return xmax, ymax, xmin, ymin


def peaks_energy(y_max, y_min):

    square_max = np.zeros(len(y_max))  # Maximum squares
    square_min = np.zeros(len(y_min))  # Minimum squares

    np.square(y_max, square_max)  # Squaring maximums
    np.square(y_min, square_min)  # Squaring minimums

    energy_max = sum(square_max)
    energy_min = sum(square_min)

    return energy_max, energy_min


def peaks_stat(y_max, y_min):

    max_mean = np.mean(y_max)
    max_std = np.std(y_max)

    min_mean = np.mean(y_min)
    min_std = np.std(y_min)

    return max_mean, max_std, min_mean, min_std


def stride_time(x_max, x_min):

    all_peaks = np.append(x_max, x_min)
    all_peaks = np.sort(all_peaks)
    time_gaps1 = np.zeros(len(all_peaks)-1)
    time_gaps = np.zeros(len(all_peaks)-1)

    for i in range(len(all_peaks)-1):  # Calculating the time gaps
        gap = all_peaks[i+1] - all_peaks[i]
        np.put(time_gaps1, i, gap)

    max_gap = max(time_gaps1)

    for j in range(len(time_gaps1)):  # Eliminating the small time gaps

        if time_gaps1[j] > (max_gap-time_gaps1[j]):
            np.put(time_gaps, j, time_gaps1[j])
        else:
            np.put(time_gaps, j, 0)

    avg_time = np.sum(time_gaps) / np.count_nonzero(time_gaps)  # Calculating the average time per stride

    return avg_time

