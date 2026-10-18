from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


X = [[50], [100], [150], [200]]
y = [5, 10, 15, 20]

model = LinearRegression()
model.fit(X, y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)