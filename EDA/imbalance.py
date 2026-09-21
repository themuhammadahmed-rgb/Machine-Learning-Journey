import pandas as pd

data = {
    "Age": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    "Churn": ["No", "No", "No", "No", "No",
              "No", "No", "No", "Yes", "Yes"]
}

df = pd.DataFrame(data)

print(df["Churn"].value_counts())