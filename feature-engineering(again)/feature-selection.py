import pandas as pd

data = {
    "Study_Hours": [1, 2, 3, 4, 5],
    "Marks": [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

print(df)
correlation = df["Study_Hours"].corr(df["Marks"])
print(correlation)