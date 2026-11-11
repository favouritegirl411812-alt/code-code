
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


def kmeans():
    """Experiment 9: K-Means Clustering."""

    # Load Iris dataset
    iris = load_iris()
    X = iris.data

    # Create K-Means model
    model = KMeans(n_clusters=3, random_state=42, n_init=10)

    # Fit the model and predict clusters
    labels = model.fit_predict(X)

    # Display results
    print("K-MEANS CLUSTERING RESULTS")
    print("\nCluster Labels:")
    print(labels)

    print("\nFirst 10 Cluster Labels:")
    print(labels[:10])

    print("\nCluster Centers:")
    print(model.cluster_centers_)

    # Visualize clusters
    plt.scatter(
        X[:, 0],
        X[:, 1],
        c=labels,
        cmap="viridis",
        label="Data Points"
    )

    # Plot cluster centers
    plt.scatter(
        model.cluster_centers_[:, 0],
        model.cluster_centers_[:, 1],
        color="red",
        marker="X",
        s=200,
        label="Centroids"
    )

    plt.xlabel("Sepal Length")
    plt.ylabel("Sepal Width")
    plt.title("K-Means Clustering")
    plt.legend()
    plt.show()

    return model
