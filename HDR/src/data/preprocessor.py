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
		encoded_labele = self.one_hot_encode(labels)
		return encoded_images, encoded_labele
		
	def test_data_loader(self):
		images, labels = _loader.test_data()
		encoded_images = self.normalize(images)
		encoded_labele = self.one_hot_encode(labels)
		return encoded_images, encoded_labele
		
_processing = Processing()
train_data_loader = _processing.train_data_loader
test_data_loader = _processing.test_data_loader