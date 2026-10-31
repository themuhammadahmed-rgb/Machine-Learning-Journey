import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Features and target
X = churn_df.drop("churn", axis=1).values
y = churn_df["churn"].values

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Create neighbor values
neighbors = np.arange(1, 13)

# Dictionaries to store accuracies
train_accuracies = {}
test_accuracies = {}

# Loop over different k values
for neighbor in neighbors:

    # Create KNN model
    knn = KNeighborsClassifier(n_neighbors=neighbor)

    # Train the model
    knn.fit(X_train, y_train)

    # Store accuracies
    train_accuracies[neighbor] = knn.score(X_train, y_train)
    test_accuracies[neighbor] = knn.score(X_test, y_test)

# Plot results
plt.title("KNN: Varying Number of Neighbors")

plt.plot(
    neighbors,
    train_accuracies.values(),
    label="Training Accuracy"
)

plt.plot(
    neighbors,
    test_accuracies.values(),
    label="Testing Accuracy"
)

plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")

plt.legend()

plt.show()