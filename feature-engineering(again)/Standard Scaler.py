from sklearn.preprocessing import StandardScaler
import pandas as pd

data = {
    "Age": [20, 25, 30, 35, 40]
}

df = pd.DataFrame(data)

scaler = StandardScaler()

df["Age"] = scaler.fit_transform(df[["Age"]])

print(df)