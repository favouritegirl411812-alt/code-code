
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def linear_regression():
    """
    Experiment 2: Linear Regression
    Predict salary based on years of experience.
    """

    # Dataset
    experience = np.array(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ).reshape(-1, 1)

    salary = np.array([
        45000, 50000, 60000, 65000, 70000,
        75000, 80000, 85000, 90000, 95000
    ])

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        experience,
        salary,
        test_size=0.2,
        random_state=42
    )

    # Create and train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Evaluation
    print("LINEAR REGRESSION RESULTS")
    print("Intercept:", model.intercept_)
    print("Coefficient:", model.coef_[0])

    print("Mean Squared Error:",
          mean_squared_error(y_test, y_pred))

    print("R2 Score:",
          r2_score(y_test, y_pred))

    # Visualization
    plt.scatter(experience, salary, color="blue",
                label="Actual Data")

    plt.plot(
        experience,
        model.predict(experience),
        color="red",
        label="Regression Line"
    )

    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.title("Linear Regression")
    plt.legend()
    plt.show()

    return model
