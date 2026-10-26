from sklearn.neighbors import KNeighborsClassifier

X = churn_df[["total_day_charge", "total_eve_charge"]].values

y = churn_df["churn"].values

print(X.shape, y.shape)

knn = KNeighborsClassifier(n_neighbors=15)

knn.fit(X, y)