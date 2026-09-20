import pandas as pd

data = {
    "Price": [100, 200, 300],
    "Quantity": [2, 3, 4]
}

df = pd.DataFrame(data)

df["Total"] = df["Price"] * df["Quantity"]

print(df)