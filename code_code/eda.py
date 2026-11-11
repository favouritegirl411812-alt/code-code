
import warnings

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def eda(file_path="Toyota.csv"):
    """
    Experiment 1(a): Exploratory Data Analysis
    Loads a dataset and performs descriptive analysis and visualization.
    """

    warnings.filterwarnings("ignore")
    sns.set_theme(style="whitegrid")

    # Load dataset
    df = pd.read_csv(file_path)

    print("\nDATASET")
    print(df)

    print("\nFIRST 5 ROWS")
    print(df.head(5))

    print("\nLAST 5 ROWS")
    print(df.tail(5))

    print("\nSHAPE")
    print(df.shape)

    print("\nNUMERICAL COLUMNS")
    print(df.select_dtypes(exclude=["object"]).columns.tolist())

    # Numerical summary
    mi = df.select_dtypes(exclude=["object"])

    print("\nMINIMUM VALUES")
    print(mi.min())

    print("\nMAXIMUM VALUES")
    print(mi.max())

    print("\nMODE")
    print(mi.mode())

    print("\nMISSING VALUES")
    print(df.isnull().sum())

    # Boxplot
    df.boxplot(figsize=(5, 5), rot=90, fontsize=8, grid=False)
    plt.title("Boxplot")
    plt.tight_layout()
    plt.show()

    # Z-score for KM
    if "KM" in df.columns:
        mean = np.mean(df["KM"])
        std = np.std(df["KM"])

        print("\nZ-SCORE")
        if std != 0:
            print((df["KM"] - mean) / std)
            df["KM-z_score"] = (df["KM"] - mean) / std
        else:
            print("Z-score cannot be calculated because standard deviation is zero.")

        print(df.head(5))

    # Correlation
    print("\nCORRELATION")
    print(df.corr(numeric_only=True))

    # Distribution plot
    if "HP" in df.columns:
        sns.displot(data=df, x="HP", kde=True, fill=True)
        plt.show()

    # Automatic value count
    if "Automatic" in df.columns:
        df["Automatic"].value_counts().plot(kind="bar")
        plt.title("Automatic Value Count")
        plt.xlabel("Automatic")
        plt.ylabel("Count")
        plt.show()

    # Swarmplot and violin plot
    if "Price" in df.columns:
        price_sample = df["Price"].dropna().sample(
            min(300, df["Price"].dropna().shape[0]),
            random_state=42
        )

        plt.figure(figsize=(10, 5))

        plt.subplot(1, 2, 1)
        sns.swarmplot(x=price_sample)

        plt.subplot(1, 2, 2)
        sns.violinplot(x=df["Price"])

        plt.tight_layout()
        plt.show()

    # Scatter plot
    if "Price" in df.columns and "HP" in df.columns:
        df.plot("Price", "HP", kind="scatter")
        plt.show()

    # Bar plot
    if "Price" in df.columns and "HP" in df.columns:
        plt.figure(figsize=(15, 10))

        sns.barplot(
            x="Price",
            y="HP",
            data=df.iloc[15:35],
            palette="plasma"
        )

        plt.show()

    # Count plot
    if "Weight" in df.columns:
        sns.countplot(x=df["Weight"])
        plt.show()

    # Pair plot
    numeric_df = df.select_dtypes(include=np.number)

    if not numeric_df.empty:
        pair_sample = numeric_df.sample(
            min(200, len(numeric_df)),
            random_state=42
        )

        sns.pairplot(pair_sample)
        plt.show()

    # Bar chart using value counts
    if "Automatic" in df.columns:
        counts = df["Automatic"].value_counts()

        plt.bar(counts.index.astype(str), counts.values)
        plt.xlabel("Automatic")
        plt.ylabel("Counts")
        plt.title("Automatic Counts")
        plt.show()

    print("\nEXPERIMENT COMPLETED")
