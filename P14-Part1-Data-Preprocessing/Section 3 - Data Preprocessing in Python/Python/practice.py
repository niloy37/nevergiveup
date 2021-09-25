<<<<<<< HEAD
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
=======
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
>>>>>>> 475384a (done)
Y = dataset.iloc[:, 3].values