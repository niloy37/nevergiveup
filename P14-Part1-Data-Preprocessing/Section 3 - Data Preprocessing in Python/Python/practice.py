
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#importing the libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#importing the dataset

dataset = pd.read_csv('C:/Data.csv')
X = dataset.iloc[:, :-1].values

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#importing the libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#importing the dataset

dataset = pd.read_csv('C:/Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values


from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])