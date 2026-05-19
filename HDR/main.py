from src.core import Loss
import numpy as np


loss = Loss()

y_pred = np.array([[1.0, -2.0, 3.0]])
y_actual = np.array([[0, -2.0, 2.0]])

cross_entropy_loss = loss.cross_entropy(y_actual, y_pred)
derivative = loss.cross_entropy_derivative(y_actual, y_pred)

print(f"""
This is the loss: {cross_entropy_loss}
This is the derivative of loss function: {derivative}
""")