
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def knn():
    """Experiment 5: K-Nearest Neighbors."""

    iris = load_iris()
    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=24
    )

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("K-NEAREST NEIGHBORS RESULTS")
    print("Actual values:", y_test)
    print("Predicted values:", y_pred)
    print("Accuracy:", accuracy_score(y_test, y_pred))

    return model
