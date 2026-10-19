
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

X = [[50], [100], [150], [200]]
y = [5, 10, 15, 20]

# 1. Split the data first
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 2. Train using only the training data
model = LinearRegression()
model.fit(X_train, y_train)

# 3. Predict the test prices
predictions = model.predict(X_test)

# 4. Evaluate the predictions
mae = mean_absolute_error(y_test, predictions)
print("Predictions:", predictions)
print("Actual prices:", y_test)
print("Test MAE:", mae)
