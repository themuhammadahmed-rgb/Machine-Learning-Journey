import pandas as pd

data = {
    "Salary": ["50000", "60000", "70000"]
}

df = pd.DataFrame(data)

print(df.dtypes) 

df["Salary"] = df["Salary"].astype(int)

print(df.dtypes)