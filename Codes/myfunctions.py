from scipy.signal import kaiserord, lfilter, firwin


def signal_arrange(signal_data):

    sensitivity = 0.000125  # V/bit | Convert to a Voltage Signal

    signal_data = [ele*sensitivity for ele in signal_data]
    mean = sum(signal_data)/len(signal_data)

    # Removing the Mean from the Signal
    new_signal = [ele-mean for ele in signal_data]

    return new_signal


def filter_fir(signal):  # Design of FIR Filter for Smoothing the Signal

    sample_rate = 110.0  # Sample Rate keep as 110Hz because Data Sample Rate is 50 Hz
    nyq_rate = sample_rate / 2.0

    width = 10.0 / nyq_rate
    ripple_db = 20.0
    n, beta = kaiserord(ripple_db, width)  # Calculating the order(n) and the beta parameter of the filter

    cutoff_hz = 15.0
    taps = firwin(n, cutoff_hz / nyq_rate, window=('kaiser', beta))
    filtered_signal = lfilter(taps, 0.5, signal)  # Filtering the signal with FIR LPF

    return filtered_signal



