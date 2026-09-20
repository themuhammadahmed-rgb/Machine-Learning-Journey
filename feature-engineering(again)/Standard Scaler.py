from sklearn.preprocessing import StandardScaler

data = {
    "Age": [20, 25, 30, 35, 40]
}

df = pd.DataFrame(data)

print(df)

scaler = StandardScaler()