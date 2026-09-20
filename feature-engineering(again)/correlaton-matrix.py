import pandas as pd


data = {
    "Age": [25, 30, 35, 40, 45],
    "Salary": [30000, 40000, 50000, 60000, 70000],
    "Experience": [2, 5, 8, 11, 14]
}

df = pd.DataFrame(data)

print(df.corr())