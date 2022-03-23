from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np

# Load iris data.
iris_dataset = load_iris()

# Get x,y training and testing data.
X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"])


# Init KNN and train x and y.
kn = KNeighborsClassifier(n_neighbors=1)
kn.fit(X_train, y_train)

# Predict
for i in range(len(X_test)):
    x = X_test[i]
    # Predict needs 2d array so we create array of array.
    x_new = np.array([x])
    prediction = kn.predict(x_new)
    print("\n Actual :", y_test[i], iris_dataset["target_names"][y_test[i]])
    print("Predicted :", prediction, iris_dataset["target_names"][prediction])
print("\n TEST SCORE[ACCURACY]: {:.2f}\n".format(kn.score(X_test, y_test)))
