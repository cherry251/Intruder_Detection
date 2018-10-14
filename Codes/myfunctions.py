# Functions required to generate time domain & frequency domain features are developed in this library
# 1.) Signal arranging function
# 2.) FIR filter
# 3.) Peak detector function

from scipy.signal import kaiserord, lfilter, firwin
from math import isnan
from pylab import *
import csv


def signal_arrange(signal_data):

    sensitivity = 0.000125  # V/bit | Convert to a Voltage Signal
    time_series = range(188)
    time_series = [ele*0.01 for ele in time_series]

    signal_data = [ele*sensitivity for ele in signal_data]
    mean_value = sum(signal_data)/len(signal_data)

    # Removing the Mean from the Signal
    new_signal = [ele-mean_value for ele in signal_data]

    return time_series, new_signal, mean_value


def filter_fir(signal):  # Design of FIR Filter for Smoothing the Signal

    sample_rate = 110.0  # Sample Rate keep as 110Hz because Data Sample Rate is 50 Hz
    nyq_rate = sample_rate / 2.0

    width = 10.0 / nyq_rate
    ripple_db = 40.0
    n, beta = kaiserord(ripple_db, width)  # Calculating the order(n) and the beta parameter of the filter

    cutoff_hz = 15.0
    taps = firwin(n, cutoff_hz / nyq_rate, window=('kaiser', beta))
    filtered_signal = lfilter(taps, 0.1, signal)  # Filtering the signal with FIR LPF

    return filtered_signal


def peak_detector(v, delta, thresh, x):  # Signal, Delta Parameter, Threshold, Independent Variable

    delta = abs(delta)
    maxtab = []
    mintab = []

    v = asarray(v)

    mn, mx = v[0], v[0]
    mnpos, mxpos = NaN, NaN

    lookformax = True

    for i in arange(len(v)):
        this = v[i]

        if abs(this) > thresh:
            if this > mx:
                mx = this
                mxpos = x[i]

            if this < mn:
                mn = this
                mnpos = x[i]

            if lookformax:
                if this < mx-delta:
                    if (mx > abs(thresh)) and not isnan(mxpos):
                        maxtab.append((mxpos, mx))
                    mn = this
                    mnpos = x[i]
                    lookformax = False
            else:
                if this > mn+delta:
                    if (mn < -abs(thresh)) and not isnan(mnpos):
                        mintab.append((mnpos, mn))
                    mx = this
                    mxpos = x[i]
                    lookformax = True

    return maxtab, mintab  # Return 2 lists with index and value


def feature_csv(dc_level, energy_max, energy_min, max_mean, max_std, min_mean, min_std, avg_stride_time, spec_centroid,
                avg_amplitude,signal_power, person):

    csv_row = [dc_level, energy_max, energy_min, max_mean, max_std, min_mean, min_std, avg_stride_time, spec_centroid,
               avg_amplitude, signal_power, person]

    csv_file = 'newset.csv'

    with open(csv_file, 'a') as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(csv_row)
