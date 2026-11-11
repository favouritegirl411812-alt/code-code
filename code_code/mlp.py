
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def mlp():
    """Experiment 4: Multilayer Perceptron using Backpropagation."""

    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42
    )

    # Create MLP model
    model = MLPClassifier(
        hidden_layer_sizes=(10,),
        activation="relu",
        max_iter=1000,
        random_state=42
    )

    # Train model
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    print("MULTILAYER PERCEPTRON RESULTS")
    print("Actual values:", y_test)
    print("Predicted values:", y_pred)
    print("Accuracy:", accuracy)

    return model
