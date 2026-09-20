import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Age" : [25, 30, 35, 40, 45]
}

df = pd.DataFrame(data)

print(df["Age"].hist())
plt.show()