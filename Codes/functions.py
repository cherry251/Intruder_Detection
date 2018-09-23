from scipy.signal import kaiserord, lfilter, firwin


def filter_fir(signal_data):  # Design of FIR Filter for Smoothing the Signal

    sample_rate = 110.0  # Sample Rate keep as 110Hz because Data Sample Rate is 50 Hz
    nyq_rate = sample_rate / 2.0

    width = 5.0 / nyq_rate
    ripple_db = 20.0
    n, beta = kaiserord(ripple_db, width)

    cutoff_hz = 10.0
    taps = firwin(n, cutoff_hz / nyq_rate, window=('kaiser', beta))
    filtered_signal = lfilter(taps, 0.5, signal_data)

    return filtered_signal


def signal_arrange(raw_signal):

    sensitivity = 0.000125  # V/bit | Convert to a Voltage Signal

    raw_signal = [ele*sensitivity for ele in raw_signal]

    mean = sum(raw_signal)/len(raw_signal)

    # Removing the Mean from the Signal
    new_signal = raw_signal - mean

    return new_signal
