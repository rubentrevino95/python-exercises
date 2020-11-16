import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")

# .head prints out first 5 elements of dataframe
print(data.head())

# data attributes
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

# split to 4 different arrays
x_train, y_train, x_test, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)