from src.model import Initializer

initial = Initializer()

w_1, w_2 = initial.initialize_weights()
b_1, b_2 = initial.initialize_biases()

print(b_1)