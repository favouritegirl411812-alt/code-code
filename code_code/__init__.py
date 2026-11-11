
from pathlib import Path

_EXPERIMENTS = {
    "eda": "eda.py",
    "preprocessing": "preprocessing.py",
    "regression": "regression.py",
    "perceptron": "perceptron.py",
    "mlp": "mlp.py",
    "knn": "knn.py",
    "svr": "svr.py",
    "fuzzy_sets": "fuzzy_sets.py",
    "naive_bayes": "naive_bayes.py",
    "kmeans": "kmeans.py",
    "dfs": "dfs.py",
    "bfs": "bfs.py",
}


def show(experiment):
    """Display the complete source code of an experiment."""

    experiment = experiment.lower().strip()

    if experiment not in _EXPERIMENTS:
        print("Experiment not found.")
        print("Available experiments:", ", ".join(_EXPERIMENTS))
        return

    file_path = Path(__file__).parent / _EXPERIMENTS[experiment]

    print(f"\n{'=' * 60}")
    print(f"EXPERIMENT: {experiment.upper()}")
    print(f"{'=' * 60}")

    if not file_path.exists():
        print("Code file not found:", file_path.name)
        return

    source = file_path.read_text(encoding="utf-8")

    if not source.strip():
        print("This experiment file is empty.")
        return

    print(source)


def show_all():
    """Display the source code of all experiments."""

    for experiment in _EXPERIMENTS:
        show(experiment)


__all__ = ["show", "show_all"]
