# Functions required to generate time domain & frequency domain features are developed in this library
# 1.) Signal arranging function
# 2.) FIR filter
# 3.) Peak detector function

from scipy.signal import kaiserord, lfilter, firwin
from math import isnan
from pylab import *
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler


def signal_arrange(signal_data):

    sensitivity = 0.000125  # V/bit | Convert to a Voltage Signal
    time_series = range(400)
    time_series = [ele*0.01 for ele in time_series]

    signal_data = [ele*sensitivity for ele in signal_data]
    mean_value = sum(signal_data)/len(signal_data)

    # Removing the Mean from the Signal
    new_signal = [ele-mean_value for ele in signal_data]

    return time_series, new_signal, mean_value


def filter_fir(signal):  # Design of FIR Filter for Smoothing the Signal

    sample_rate = 220.0
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

    csv_file = 'Features_6.csv'

    with open(csv_file, 'a') as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow(csv_row)


def knn_classifier(x_train, x_test, y_train, y_test):

    knn = KNeighborsClassifier()
    knn.fit(x_train, y_train)

    training_accuracy = knn.score(x_train, y_train)
    test_accuracy = knn.score(x_test, y_test)
    print('Accuracies Training/Test KNN :')
    print(training_accuracy)
    print(test_accuracy)
    print('______________________________________')

    training_probability = knn.predict_proba(x_train[:5])
    test_probability = knn.predict_proba(x_test[:5])
    print('Probabilities Training/Test KNN :')
    print(training_probability)
    print(test_probability)
    print('______________________________________')

    return training_accuracy, test_accuracy, training_probability, test_probability


def dt_classifier(x_train, x_test, y_train, y_test):

    tree = DecisionTreeClassifier(max_depth= 6, random_state=42)
    tree.fit(x_train, y_train)

    training_accuracy = tree.score(x_train, y_train)
    test_accuracy = tree.score(x_test, y_test)
    print('Accuracies Training/Test DT :')
    print(training_accuracy)
    print(test_accuracy)
    print('______________________________________')

    training_probability = tree.predict_proba(x_train[:5])
    test_probability = tree.predict_proba(x_test[:5])
    print('Probabilities Training/Test DT :')
    print(training_probability)
    print(test_probability)
    print('______________________________________')

    return training_accuracy, test_accuracy, training_probability, test_probability


def svm_classifier(x_train, x_test, y_train, y_test):

    svm = SVC(C=1000, random_state=42)
    svm.fit(x_train, y_train)

    min_train = x_train.min(axis=0)
    range_train = (x_train - min_train).max(axis=0)
    x_train_scaled = (x_train - min_train)/range_train
    x_test_scaled = (x_test - min_train)/range_train

    training_accuracy = svm.score(x_train_scaled, y_train)
    test_accuracy = svm.score(x_test_scaled, y_test)

    print('Accuracies Training/Test SVM :')
    print(training_accuracy)
    print(test_accuracy)
    print('______________________________________')

    # training_probability = svm.predict_proba(x_train_scaled[:5])
    # test_probability = svm.predict_proba(x_test_scaled[:5])

    return training_accuracy, test_accuracy


def nn_classifier(x_train, x_test, y_train, y_test):

    scaler = StandardScaler()
    x_train_scaled = scaler.fit(x_train).transform(x_train)
    x_test_scaled = scaler.fit(x_test).transform(x_test)
    nn = MLPClassifier(max_iter=4000, alpha=1, random_state=30)
    nn.fit(x_train_scaled, y_train)

    training_accuracy = nn.score(x_train_scaled, y_train)
    test_accuracy = nn.score(x_test_scaled, y_test)
    print('Accuracies Training/Test NN :')
    print(training_accuracy)
    print(test_accuracy)
    print('______________________________________')
    training_probability = nn.predict_proba(x_train_scaled[:3])
    test_probability = nn.predict_proba(x_test_scaled[:3])
    training_probability = [ele*100 for ele in training_probability]
    test_probability = [ele*100 for ele in test_probability]
    print('Probabilities of Training/Test NN :')
    print(training_probability)
    print(test_probability)
    print('______________________________________')

    return training_accuracy, test_accuracy, training_probability, test_probability



