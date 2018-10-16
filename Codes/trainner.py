import pandas as pd
from sklearn.model_selection import train_test_split
from myfunctions import knn_classifier, dt_classifier, svm_classifier, nn_classifier

raw_data = pd.read_csv('Features_5.csv', delimiter=',', header=None)
raw_data = raw_data.dropna()
# raw_data = raw_data.reset_index()
raw_data1 = raw_data.values
data = raw_data1[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
targets = raw_data1[:, 11]

x_train, x_test, y_train, y_test = train_test_split(data, targets, stratify=targets, random_state=0)

# KNN Classifier
training_acc_knn, test_acc_knn, training_prob_knn, test_prob_knn = knn_classifier(x_train, x_test, y_train, y_test)

# Decision Tree Classifier
training_acc_dt, test_acc_dt, training_prob_dt, test_prob_dt = dt_classifier(x_train, x_test, y_train, y_test)

# SVM Classifier
training_acc_svm, test_acc_svm = svm_classifier(x_train, x_test, y_train, y_test)

# Neural Network Classifier
training_acc_nn, test_acc_nn, training_prob_nn, test_prob_nn = nn_classifier(x_train, x_test, y_train, y_test)
