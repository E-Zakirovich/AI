from src.core import Metrics
import numpy as np

accuracy_level = Metrics()

y_pred = np.array(
[
	[0.8, 0.1, 0.1], 
	[0.1, 3.0, 6.0], 
	[0.1, 0.0, 9.0], 
	[0.1, 8.0, 0.1]
]
)

y_actual = np.array(
[
	[1.0, 0.0, 0.4], 
	[0.0, 1.0, 0.0], 
	[0.0, 0.0, 1.0], 
	[0.0, 1.0, 0.0]
]
)

p = accuracy_level.accuracy(y_pred, y_actual)

print("Accuracy:", p)
