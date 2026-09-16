import pandas as pd

data = {
    "Age": [20, 25, 30, 35],
    "Salary": [50000, None, 70000, None]
}
df = pd.DataFrame(data)

print(df.isnull())
print(df.isnull().sum())

print(df.dropna())  # Drop rows with any null values