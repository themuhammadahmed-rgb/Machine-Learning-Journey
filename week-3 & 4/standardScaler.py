from sklearn.preprocessing import StandardScaler

data = [[10], [20], [30]]

scaler = StandardScaler()
result = scaler.fit_transform(data)
print(result)