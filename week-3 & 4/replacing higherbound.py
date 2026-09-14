import numpy as np

data = np.array([10, 12, 13, 15, 16, 18, 100])


q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)


iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
higher_bound = q3 + 1.5 * iqr

replace = np.where(data > higher_bound, higher_bound, data)

print("Replaced Data:", replace)