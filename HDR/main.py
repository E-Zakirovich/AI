from src.loader import Loader

a = Loader()


p = a.train_dataset()

print(p[0][0])