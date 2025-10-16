import numpy as np 

data = iris_2d = np.genfromtxt("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", delimiter=',', dtype='float', usecols=[1, 3])
print(data)