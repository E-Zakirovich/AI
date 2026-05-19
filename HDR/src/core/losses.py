"""
losses.py
~~~~~~~~~~

My model is predicting according to my image pixels that I entered before but how can I know that 
how my network is performing well? To know this I am going to use cost function. The type of cost
 function is Cross Entropy

I am going to create a class called Loss. Inside of this this class following methods created:
- cross_entropy(y_predicted, y_actual)
- cross_entropy_derivative(y_predicted, y_actual)

cross_entropy(y_predicted, y_actual) - it will help me to calculate cost function. There is some 
mathematical background you need to know about it, thats why follow the link below
https://en.wikipedia.org/wiki/Cross-entropy

cross_entropy_derivative(y_predicted, y_actual) - this will help me to calculate derivative of loss function (I will use it in backpropagation algorithm, it is a bit tough. I will explain this part in network training session).
"""

import numpy as np

class Loss:
	
	def cross_entropy(self, y_actual, y_pred):
		n = y_pred.shape[0]
		log_pred = np.log(y_pred + 1e-08)
		return -np.sum(y_actual * log_pred) / n
		
	def cross_entropy_derivative():
		return y_pred - y_actual