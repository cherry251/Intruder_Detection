# Frequency Domain Features
# The Spectral Centroid
# Power Spectral Density
# Average Amplitude

from __future__ import division
from numpy import abs, sum, linspace, sort
from numpy.fft import rfft


def spectral_extracts(filtered_signal):

    spectrum = abs(rfft(filtered_signal))
    norm_spectrum = spectrum / max(spectrum)
    norm_frequencies = linspace(0, 1, len(spectrum))
    spec_centroid = sum(norm_frequencies * norm_spectrum) / sum(norm_spectrum)
    power_spectrum = spectrum ** 2

    new_spectrum = sort(norm_spectrum)
    avg_amplitude = sum(new_spectrum[0:35]) / len(new_spectrum[0:35])
    avg_amplitude = avg_amplitude * max(spectrum)

    return norm_spectrum, norm_frequencies, power_spectrum, spec_centroid, avg_amplitude
