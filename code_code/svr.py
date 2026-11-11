
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score


def svr():
    """Experiment 6: Support Vector Regression."""

    # Load Iris dataset
    iris = load_iris()
    X = iris.data

    # Use sepal width as the target
    y = X[:, 1]

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.1, random_state=42
    )

    # Create and train the SVR model
    model = SVR(kernel="linear")
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    print("SUPPORT VECTOR REGRESSION RESULTS")
    print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
    print("R2 Score:", r2_score(y_test, y_pred))

    # Visualize actual and predicted values
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Values")
    plt.ylabel("Predicted Values")
    plt.title("Support Vector Regression")
    plt.show()

    return model
