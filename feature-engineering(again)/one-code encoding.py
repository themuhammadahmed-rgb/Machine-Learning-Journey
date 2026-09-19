import pandas as pd

data = {
    "City": ["Lahore", "Karachi", "Islamabad", "Lahore"]
}

df = pd.DataFrame(data)

print(df)

df_encoded = pd.get_dummies(df, columns=["City"])
print(df_encoded)