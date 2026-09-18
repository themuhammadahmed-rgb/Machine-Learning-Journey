import pandas as pd

data = {
    "Age": [20, 25, -3, 30]
}

df = pd.DataFrame(data)

print(df)

print(df["Age"] > 0)

df.loc[df["Age"] <= 0, "Age"] = None      