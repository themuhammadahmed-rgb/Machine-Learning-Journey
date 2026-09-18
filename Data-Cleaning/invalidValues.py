import pandas as pd

data ={
    "Age" : [20, 25, -3, 30]
}

df = pd.DataFrame(data)

print(df["Age"] > 0)