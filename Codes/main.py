import pandas as pd
from pylab import figure, plot, show
from myfunctions import filter_fir, signal_arrange
from timedomainfeatures import find_peaks

Signal_df = pd.read_excel("D:\Academics\EE 405\August Start\Intruder Detection\MLCode\DataFiles\RawSignals.xlsx",
                          sheet_name=0)
lengths = list(Signal_df)

for i in range(31):
    SignalData = Signal_df.iloc[0:188, i].values

    Signal = signal_arrange(SignalData)
    filteredSignal = filter_fir(Signal)
    indexes = find_peaks(filteredSignal, i)

    #figure(i)
    #plot(Signal)
    #plot(filteredSignal)
    #show()




