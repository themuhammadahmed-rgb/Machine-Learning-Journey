import pandas as pd


data = {
    "Age" : [25, 30, 35, 40, 45]
}

df = pd.DataFrame(data)

print(df["Age"].describe())