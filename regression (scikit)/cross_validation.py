from sklearn.model_selection import KFold, cross_val_score


kf = KFold(n_splits=5, shuffle=True, random_state=42)



reg = LinearRegression()


cv_scores = cross_val_score(reg, X, y, cv=kf)



# Print scores
print(cv_scores)