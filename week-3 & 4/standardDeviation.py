import numpy as np


data = np.array([10, 20, 30])

mean = np.mean(data)
std = np.std(data)


standardized_data = (data - mean) / std

print(standardized_data) 