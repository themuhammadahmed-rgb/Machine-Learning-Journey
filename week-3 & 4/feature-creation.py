import pandas as pd

data = {
    "Height" : [1.8, 1.6, 1.75],
    "Weight" : [80, 60, 75]
}

df = pd.DataFrame(data)
df["BMI"] = df["Weight"] / (df["Height"] ** 2)

print(df)