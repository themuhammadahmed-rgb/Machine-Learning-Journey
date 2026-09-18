import pandas as pd

data = {
    "Name": ["Ali", "Ahmed", "Ali", "Sara"],
    "Age": [22, 25, 22, 30],
    "Salary": [50000, 60000, 50000, 80000]
}

df = pd.DataFrame(data)

pd.to_numeric(df["Salary"], errors='coerce')