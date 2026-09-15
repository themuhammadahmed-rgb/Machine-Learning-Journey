from sklearn.preprocessing import MinMaxScaler

data = [[10], [20], [30]]

scaler = MinMaxScaler()

result = scaler.fit_transform(data)

print(result)
