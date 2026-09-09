import pandas as pd

data = {
    "Name": ["Ahmed", "Ali", "Hamza"],
    "Age": [20, 21, 19],
    "Grade": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)