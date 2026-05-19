"""
preprocessor.py
~~~~~~~~~~~~~~~

This folder is going to help me to encode MNIST dataset. There is four 
methods created. They are:
	
	normalize(images) - help you to squeeze values from 0 - 255 to 0 - 1
	
	one_hot_encode(labels) - help you to encode labels from just number to array form. 
	example 5 -> [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
	
	train_data_loader() - it will use normalize(images) and one_hot_encode(labels) methods 
	then it will return images and labels at the same time. 
	
	test_data_loader() - it works same as train_data_loader() method. 
"""


from config import MAX_GREYSCALE, NUM_CLASSES
import numpy as np
from .loader import Loader

_loader = Loader()

class Processing:
	
	def normalize(self, images):
		return images / MAX_GREYSCALE
		
	def one_hot_encode(self, labels):
		one_hot = np.zeros((labels.shape[0], NUM_CLASSES))
		one_hot[np.arange(labels.shape[0]), labels] = 1
		return one_hot
		
	def train_data_loader(self):
		images, labels = _loader.train_data()
		encoded_images = self.normalize(images)
		encoded_labels = self.one_hot_encode(labels)
		return encoded_images, encoded_labels
		
	def test_data_loader(self):
		images, labels = _loader.test_data()
		encoded_images = self.normalize(images)
		encoded_labels = self.one_hot_encode(labels)
		return encoded_images, encoded_labele
		
_processing = Processing()
train_data_loader = _processing.train_data_loader
test_data_loader = _processing.test_data_loader