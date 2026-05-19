from src.core import ActivationFunctions
import numpy as np

Z = np.array([[1.0, -2.0, 3.0]])

activators = ActivationFunctions()

relu_value = activators.ReLU(Z)

derivative_relu = activators.ReLU_Derivation(Z)

softmax_value = activators.softmax(Z)

print(f"""
ReLU: {relu_value}
Derivative of ReLU: {derivative_relu}
Softmax: {softmax_value}
""")