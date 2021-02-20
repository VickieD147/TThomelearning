import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
dataset = pd.read_csv("student_scores.csv")
print(dataset.shape)
print(dataset.head())
print(dataset.describe())
dataset.plot(x="Hours", y="Scores", style='o')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.title('Hours vs Percentages')
plt.show()
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, :1].values
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print("intercept", regressor.intercept_)
print("coef :", regressor.coef_)
y_pred = regressor.predict(X_test)
print('ytest', y_test, 'y pred', y_pred)
data = {'Actual': [1.5, 3.2, 7.4, 2.5, 5.9],
        'Predicted': [1.5, 3.2, 7.4, 2.5, 5.9]}
df = pd.DataFrame(data)
print(df.shape)
print(df)
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
