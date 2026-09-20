import pandas as pd

data = {
    "Age": [25, 30, 35, 40, 45],
    "Years_Experience": [3, 8, 13, 18, 23]
}

df = pd.DataFrame(data)

correlation = df["Age"].corr(df["Years_Experience"])

print(correlation)