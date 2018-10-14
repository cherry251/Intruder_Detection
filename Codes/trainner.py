import numpy as np
import pandas_ml as pdml
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

raw_data = pd.read_csv('newset.csv', delimiter=',', header=None)
raw_data = raw_data.dropna()
# raw_data = raw_data.reset_index()
raw_data1 = raw_data.values
data = raw_data1[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
targets = raw_data1[:, 11]

x_train, x_test, y_train, y_test = train_test_split(data, targets, stratify=targets, random_state=42)

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

print(knn.score(x_train, y_train))
print(knn.score(x_test, y_test))
