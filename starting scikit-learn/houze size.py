from sklearn.linear_model import LinearRegression

X = [[50], [100], [150], [200]]
y = [5, 10, 15, 20]

model = LinearRegression()
model.fit(X, y)



prediction1 = model.predict([[250]])
print(prediction1)


prediction2 = model.predict([[80]])
print(prediction2)

prediction3 = model.predict([[120]])
print(prediction3)

print(model.coef_)
print(model.intercept_)


predictions = model.predict(X)
print(predictions)
