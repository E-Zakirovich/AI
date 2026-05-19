"""
activation_functions.py
~~~~~~~~~~~~~~~~~~~~~~~~

Basically,  each neuron has  activation functions.  For example sigmoid, tanh,  relu and so on. 
Because of this my neural network will learn. I choose ReLU neurons, for output neuron Softmax. 
I created three methods.

I need a class for make activations functions. ActivationFunctions is the name of the class. 
Inside of this class I created three methods. They are:

relu(Z) - this method is activation function for calculate weighted sum Z. My network is 
learning because of relu(Z) activation function. Here Z is weighted sum, it is coming 
from neurons.  

derivative_relu(Z) - it will help me while I am training my network. I will use this method 
with backpropagation algorithm. It will help me to improve correctness of the net. Z is 
mentioned in relu(Z) method explanation.

softmax(Z) - this method will help me to make a decision. In output layer, I am going to have
 total ten neurons. Each neuron will return their prediction. Sum of predictions going to be 
 higher than one and it is not accurate to get highest predicted value as a result. In this 
 case, I need to squeeze all results. After squeeze them sum of neurons going to be 1. Then 
 I will pick up most high predicted value. Formula - search it https://en.wikipedia.org/wiki/Softmax_function
 """

import numpy as np

class ActivationFunctions:
	
	def ReLU(self, Z):
		pass
		
	def ReLU_Derivation(self, Z):
		pass
		
	def softmax(Z):
		pass