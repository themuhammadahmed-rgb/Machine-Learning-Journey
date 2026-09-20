import pandas as pd

data = {
    "Level": ["Beginner", "Advanced", "Intermediate", "Beginner", "Advanced"]
}

df = pd.DataFrame(data)

level_map = {
    "Beginner" : 1,
    "Intermediate" : 2,
    "Advanced" : 3
}

df["level"] = df["level"].map(level_map)
print(df)