import numpy as np
import pandas as pd
from pylab import figure, plot, show
from functions import filter_fir, signal_arrange

Signal_df = pd.read_excel("D:\Academics\EE 405\August Start\Intruder Detection\MLCode\DataFiles\RawSignals.xlsx",
                          sheet_name=0)
lengths = list(Signal_df)

for i in range(31):
    SignalData = Signal_df.iloc[0:260, i].values



    figure(i)
    plot(SignalData)
    show()



