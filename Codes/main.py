import pandas as pd
from pylab import figure, plot, show, grid, stem
from myfunctions import filter_fir, signal_arrange, feature_csv
from timedomainfeatures import find_peaks, peaks_energy, peaks_stat, stride_time
from frequencydomainfeatures import spectral_extracts
# from training import train_algorithms

Signal_df = pd.read_excel("D:\Academics\EE 405\August Start\Intruder Detection\MLCode\DataFiles\RawSignals_II.xlsx",
                          sheet_name=4)

for i in range(50):

    SignalData = Signal_df.iloc[0:400, i].values  # Extracting the signal

    # Time Domain Features
    Time, Signal, dcLevel = signal_arrange(SignalData)  # Arranging the signal, mean removed
    filteredSignal = filter_fir(Signal)  # FIR LPF, to eliminate the noise and smoothing the signal
    x_max, y_max, x_min, y_min = find_peaks(filteredSignal)  # Getting peak indexes and values
    energy_max, energy_min = peaks_energy(y_max, y_min)  # Calculating peak energy, sum(ele.*2) each max and min peaks
    max_mean, max_std, min_mean, min_std = peaks_stat(y_max, y_min)  # Calculating the means and std. of peaks
    avg_stride_time = stride_time(x_max, x_min)  # Calculating the average time per stride

    person = 4

    # Frequency Domain Features
    norm_spectrum, norm_frequencies, power_spectrum, spec_centroid, avg_amplitude, \
        signal_power = spectral_extracts(filteredSignal)
    # idx = np.argsort(norm_frequencies)

    feature_csv(dcLevel, energy_max, energy_min, max_mean, max_std, min_mean, min_std, avg_stride_time, spec_centroid,
                avg_amplitude, signal_power, person)

"""
    figure('Original and Filtered Signal')

    plot(Time, Signal)
    plot(Time, filteredSignal)
    # plot(x_max, y_max, 'r+')
    # plot(x_min, y_min, 'g+')

    figure('Normalized Frequency Spectrum')
    stem(norm_frequencies, norm_spectrum, 'b')
    figure('Power Spectral')
    stem(norm_frequencies, power_spectrum, 'r')

    grid(True)
    show()
"""



