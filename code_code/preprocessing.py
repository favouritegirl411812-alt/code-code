
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import KNNImputer


def preprocessing(file_path="Toyota.csv"):
    """
    Experiment 1(b): Data Preprocessing

    Operations:
    1. Percentage of missing values
    2. Mean imputation
    3. Mode imputation
    4. KNN imputation
    5. Drop columns with more than 10% missing values
    6. Outlier removal using Z-score
    7. Duplicate removal
    8. Min-Max normalization
    9. One-hot encoding
    """

    sns.set_theme(style="whitegrid")

    # Load dataset
    df = pd.read_csv(file_path)

    print("\nORIGINAL DATASET")
    print(df.head())

    # 1. Percentage of missing values
    print("\n1. PERCENTAGE OF MISSING VALUES")

    missing = df.isnull().sum()
    percentage = (missing / len(df)) * 100

    print(percentage)

    # 2. Mean imputation if below 10%
    print("\n2. MEAN IMPUTATION")

    for col in df.columns:
        if (
            percentage[col] < 10
            and pd.api.types.is_numeric_dtype(df[col])
            and df[col].isnull().sum() > 0
        ):
            df[col] = df[col].fillna(df[col].mean())

    print(df.isnull().sum())

    # 3. Mode imputation for categorical data
    print("\n3. MODE IMPUTATION")

    categorical_columns = df.select_dtypes(
        include=["object", "string", "category"]
    ).columns

    for col in categorical_columns:
        if df[col].isnull().sum() > 0:
            mode_values = df[col].mode()

            if not mode_values.empty:
                df[col] = df[col].fillna(mode_values[0])

    print(df.isnull().sum())

    # 4. KNN imputation
    print("\n4. KNN IMPUTATION")

    knn_df = pd.read_csv(file_path)

    numeric_cols = knn_df.select_dtypes(
        include=np.number
    ).columns

    if len(numeric_cols) > 0:
        imputer = KNNImputer(n_neighbors=5)

        knn_df[numeric_cols] = imputer.fit_transform(
            knn_df[numeric_cols]
        )

    print(knn_df[numeric_cols].head())

    # 5. Drop columns with more than 10% missing values
    print("\n5. DROP COLUMNS")

    for col in df.columns.tolist():
        if percentage[col] > 10:
            df.drop(columns=[col], inplace=True)
            print(col, "Dropped")

    print("Shape of dataset:", df.shape)

    # 6. Drop rows with outlier Z-score > 3
    print("\n6. OUTLIER REMOVAL")

    if "Doors" in df.columns:
        df["Doors"] = df["Doors"].replace({
            "three": 3,
            "four": 4,
            "five": 5,
            "two": 2
        })

        df["Doors"] = pd.to_numeric(
            df["Doors"],
            errors="coerce"
        )

        mean = df["Doors"].mean()
        std = df["Doors"].std()

        if pd.notna(std) and std != 0:
            z = (df["Doors"] - mean) / std
            df = df[z.abs() <= 3]

    print("Shape after outlier removal:", df.shape)

    # 7. Drop duplicate rows
    print("\n7. DUPLICATE REMOVAL")

    df = df.drop_duplicates()

    print("Shape after removing duplicates:", df.shape)

    # 8. Min-Max normalization
    print("\n8. MIN-MAX NORMALIZATION")

    if "Price" in df.columns:
        x = df["Price"]

        if x.max() != x.min():
            xscal = (x - x.min()) / (x.max() - x.min())
        else:
            xscal = pd.Series(0, index=x.index)

        print(xscal.head())

        sns.scatterplot(x=x, y=xscal)

        plt.title("Min-Max Normalization")
        plt.xlabel("Original Price")
        plt.ylabel("Normalized Price")
        plt.show()

    # 9. One-hot encoding
    print("\n9. ONE-HOT ENCODING")

    if "FuelType" in df.columns:
        dum = pd.get_dummies(
            df["FuelType"],
            prefix="Fuel"
        )

        print(dum.head())

        df = pd.concat([df, dum], axis=1)
        df.drop(columns=["FuelType"], inplace=True)

    else:
        print("FuelType column not found")

    # Final dataset
    print("\nFINAL DATASET")
    print(df.head())

    print("Final shape:", df.shape)

    return df
