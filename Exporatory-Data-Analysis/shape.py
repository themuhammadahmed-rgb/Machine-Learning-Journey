import pandas as pd

data = {
    "Name": ["Ahmed", "Ali", "Hamza", "Usman", "Bilal"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(data)


print(df)
print(df.shape)
df.info()
print(df.describe())
print(df.isnull())
print(df.isnull().sum())
print(df.duplicated())
print(df.duplicated().sum())
print(df.dtypes)