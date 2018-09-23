import numpy as np
import pandas as pd
from pylab import figure, plot, show, grid
from myfunctions import filter_fir, signal_arrange
from timedomainfeatures import find_peaks

Signal_df = pd.read_excel("D:\Academics\EE 405\August Start\Intruder Detection\MLCode\DataFiles\RawSignals.xlsx",
                          sheet_name=0)

for i in range(31):
    SignalData = Signal_df.iloc[0:188, i].values
    Time, Signal = signal_arrange(SignalData)
    filteredSignal = filter_fir(Signal)
    xmax, ymax, xmin, ymin = find_peaks(filteredSignal)

    figure(i)
    plot(Time, Signal)
    plot(Time, filteredSignal)
    plot(xmax, ymax, 'r+')
    plot(xmin, ymin, 'g+')
    grid(True)
    show()




