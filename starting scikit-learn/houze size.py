from sklearn.linear_model import LinearRegression

X = [[50], [100], [150], [200]]
y = [5, 10, 15, 20]

model = LinearRegression()
model.fit(X, y)



prediction = model.predict([[250]])

print(prediction)