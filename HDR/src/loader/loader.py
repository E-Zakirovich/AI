"""
loader.py 
~~~~~~~~~

I created this file to load MNIST dataset, thats it.
"""

import numpy as np
import struct 
from config import TRAIN_IMAGES, TRAIN_LABELS, TEST_IMAGES, TEST_LABELS

class Loader:
	
	def read_images(self, filepath : str) -> list: 
		with open(filepath, 'rb') as f:
			magic, num, rows, cols = struct.unpack('>IIII', f.read(16))
			images = np.frombuffer(f.read(), dtype=np.uint8)
			images = images.reshape(num, rows * cols)
		return images
		
	def read_labels(self, filepath : str) -> list:
		with open(filepath, 'rb') as f:
			magic, nums = struct.unpack(">II", f.read(8))
			labels = np.frombuffer(f.read(), dtype=np.uint8)
		return labels
		
	def train_dataset(self) -> tuple[list, list]:
		images = self.read_images(TRAIN_IMAGES)
		labels = self.read_labels(TRAIN_LABELS)
		return images, labels
		
	def test_dataset(self) -> tuple[list, list]:
		images = self.read_images(TEST_IMAGES)
		labels = self.read_labels(TEST_LABELS)
		return images, labels