import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

print(df.plot.scatter(x='Study_Hours', y='Marks', title='Study Hours vs Marks'))
plt.show()