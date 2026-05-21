"""
initializer.py
~~~~~~~~~~~~~~~

I start calculations, there are several ways to choose weights and biases. I would prefer 
being smart, thats why I created separated file for initialization. I am going to use 
Xavier method to initialize weights and biases. Currently, I am not also totally 
understand philosophy behind about `Xavier`, but it is better instead of initialize 
parameters randomly. 

I am going to create a class called Initializer. Inside of this class, I will created following methods

xavier(rows, cols) - it will help you to initialize weights. This method is also based on randomness
but there is a scale that random number generated between two numbers. This method is going to return
 matrix rows x cols.

zeros(size) - it will help me to initialize bias. It will return a matrix size x 1.

initialize_weights - It will initialize weights for whole network. My network has one hidden layer, 
one output layer and one input layer. So, I need weights for between input and hidden layer. One 
for hidden and output layer. 

initialize_biases() - It will initialize weight for whole neural network. As i said before, I 
have got a hidden layer, output layer and input layer. Thats why one bias collection for between
input and hidden layer and one for between hidden and output layer.
"""

from config import INPUT_SIZE, HIDDEN_LAYER_SIZE, OUTPUT_LAYER_SIZE
import numpy as np

class Initializer:
	
	def xavier(self, rows, cols):
		limit = np.sqrt(6/(rows + cols))
		return np.random.uniform(-limit, limit, (rows, cols))
		
	def zeros(self, sizes):
		return np.zeros((1, sizes))
		
	def initialize_weights(self):
		w1 = self.xavier(INPUT_SIZE, HIDDEN_LAYER_SIZE)
		w2 = self.xavier(HIDDEN_LAYER_SIZE, OUTPUT_LAYER_SIZE)
		return w1, w2
		
	def initialize_biases(self):
		b1 = self.zeros(HIDDEN_LAYER_SIZE)
		b2 = self.zeros(OUTPUT_LAYER_SIZE)
		return b1, b2