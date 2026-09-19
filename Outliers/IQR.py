import pandas as pd

data = {
    "Salary": [50000, 52000, 48000, 55000, 51000, 5000000]
}

df = pd.DataFrame(data)

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1