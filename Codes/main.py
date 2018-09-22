import pandas as pd

Signal_df = pd.read_excel("D:\Academics\EE 405\August Start\Intruder Detection\MLCode\DataFiles\RawSignals.xlsx", sheet_name=0, header=0)

for i in range(31):
    SignalData = Signal_df.iloc[0:188, i]
    # print(SignalData)

print(type(SignalData))
