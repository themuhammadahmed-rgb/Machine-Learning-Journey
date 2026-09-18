import pandas as pd

data = {
"Gender" : ["Male", "male", "  MALE"]
}

df = pd.DataFrame(data)

df["Gender"] = df["Gender"].str.strip().str.lower()

print(df)
print(df["Gender"].value_counts())