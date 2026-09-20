import pandas as pd

data = {
    "Education": ["High School", "Bachelor", "Master", "PhD", "Bachelor"]
}

df = pd.DataFrame(data)


education_map = {
    "High School": 1,
    "Bachelor": 2,
    "Master": 3,
    "PhD": 4
}
df["Education"] = df["Education"].map(education_map)
print(df)