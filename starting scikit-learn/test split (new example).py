from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42, stratify= y
)

knn  = KNeighborsClassifier(n_neighbors = 6)
knn.fit(X_train, y_train)   

print(knn.score(X_test, y_test))