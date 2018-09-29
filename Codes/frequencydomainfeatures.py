# Frequency Domain Features
# The Spectral Centroid
# Power Spectral Density
# Average Amplitude

from __future__ import division
from numpy import abs, sum, linspace, sort
from numpy.fft import rfft, fftfreq


def spectral_extracts(filtered_signal):

    sample_time = 0.01
    spectrum = abs(rfft(filtered_signal))
    frequencies = fftfreq(spectrum.size, sample_time)

    max_amplitude = max(spectrum)
    max_frequency = max(frequencies)

    norm_spectrum = spectrum / max_amplitude
    norm_frequencies = frequencies/max_frequency

    spec_centroid = sum(norm_frequencies * norm_spectrum) / sum(norm_spectrum)
    power_spectrum = spectrum ** 2

    sorted_spectrum = sort(norm_spectrum)
    avg_amplitude = sum(sorted_spectrum[0:35]) / len(sorted_spectrum[0:35])
    avg_amplitude = avg_amplitude * max_amplitude

    signal_power = sum(power_spectrum)

    return norm_spectrum, norm_frequencies, power_spectrum, spec_centroid, avg_amplitude, signal_power
