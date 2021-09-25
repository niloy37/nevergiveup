

#importing the libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#importing the dataset

dataset = pd.read_csv('C:/Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values


from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder_x = LabelEncoder()
X[:,0]  = labelencoder_x.fit_transform(X[:,0])

ct = ColumnTransformer([("Country", OneHotEncoder(), [0])], remainder = 'passthrough')
X = ct.fit_transform(X)

labelencoder_y  = LabelEncoder()
y= labelencoder_y.fit_transform(y)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

