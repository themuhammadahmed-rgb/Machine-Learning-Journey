import pandas as pd

data = {
    "Salary": [50000, 52000, 48000, 55000, 51000, 5000000]
}

df = pd.DataFrame(data)

print(df["Salary"].describe())