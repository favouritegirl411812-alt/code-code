
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score


def perceptron():
    """Experiment 3: Perceptron Classification."""

    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Feature scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Create Perceptron model
    model = Perceptron(
        max_iter=100,
        eta0=0.1,
        random_state=0
    )

    # Train model
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)

    print("PERCEPTRON CLASSIFICATION")
    print("Actual values:", y_test)
    print("Predicted values:", y_pred)
    print("Accuracy:", accuracy)

    return model
