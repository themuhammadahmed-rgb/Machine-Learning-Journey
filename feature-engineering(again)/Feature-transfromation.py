import numpy as np
import pandas as pd
data = {
    "Salary": [100, 1000, 10000, 100000]
}

df = pd.DataFrame(data)

print(df)

df["Salary_log"] = np.log(df["Salary"])

print(df)