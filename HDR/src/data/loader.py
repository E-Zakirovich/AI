"""
loader.py
~~~~~~~~~

This folder is going to help me to import dataset from ./data folder. Inside fo this file there is a class and four methods. 
Loader class is main. It will connect to main python file caled main.py

load_images(filepath) - this file is going to help me to read images from MNIST dataset. It can read test and train images
load_labels(filepath) - this file is going to help me to read labels from MNIST dataset. It can read test and train images

train_data() - this method will use load_images(filepath), load_labels(filepath) methods and return image and labels data at
the same time. test_data() is same as train_data()
"""



from config import TEST_IMAGES, TEST_LABELS, TRAIN_IMAGES, TRAIN_LABELS
import numpy as np
import struct 

class Loader:
	def load_images(self, filepath):
		with open(filepath, 'rb') as f:
			magic, num, row, col = struct.unpack(">IIII", f.read(16))
			images = np.frombuffer(f.read(), dtype=np.uint8)
			images = images.reshape(num, row * col)
		return images
	
	def load_labels(self, filepath):
		with open(filepath, 'rb') as f:
			magic, num = struct.unpack('>II', f.read(8))
			labels = np.frombuffer(f.read(), dtype=np.uint8)
		return labels
		
	def train_data(self):
		images = self.load_images(TRAIN_IMAGES)
		labels = self.load_labels(TRAIN_LABELS)
		return images, labels
		
	def test_data(self):
		images = self.load_images(TEST_IMAGES)
		labels = self.load_labels(TEST_LABELS)
		return images, labels