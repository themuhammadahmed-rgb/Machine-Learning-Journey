from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


X = sales_df.drop("sales", axis=1).values
y = sales_df["sales"].values

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Instantiate the model
reg = LinearRegression()

# Fit the model to the training data
reg.fit(X_train, y_train)

# Make predictions using the test features
y_pred = reg.predict(X_test)

print("Predictions: {}, Actual Values: {}".format(y_pred[:2], y_test[:2])