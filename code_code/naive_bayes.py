
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


def naive_bayes():
    """Experiment 8: Naive Bayes Classification."""

    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Create and train Gaussian Naive Bayes model
    model = GaussianNB()
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    print("NAIVE BAYES CLASSIFICATION RESULTS")
    print("Actual values:", y_test)
    print("Predicted values:", y_pred)
    print("Accuracy:", accuracy_score(y_test, y_pred))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(
        y_test, y_pred, target_names=iris.target_names
    ))

    return model
