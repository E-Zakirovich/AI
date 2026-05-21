"""
metrics.py
~~~~~~~~~~~

I want to know how much my model is predicting  correctly in percentages. To get the 
result like - "my model is predicting about 96% correct" and so on. Thats why I need 
metrics.py file. 

I created a class and name it Metrics. Inside of this class there is only one method.
It is accuracy(y_pred, y_actual) and it will calculate percentage
"""

import numpy as np

class Metrics:
	def accuracy(self, y_pred, y_actual):
		predictions = np.argmax(y_pred, axis = 1)
		actual = np.argmax(y_actual, axis = 1)
		return np.mean(actual == predictions)