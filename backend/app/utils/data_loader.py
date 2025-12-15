import pandas as pd


def load_credit_data(
    file_path: str,
    test_size: float = 0.3
):
    """
    Load and preprocess the UCI Credit Card Default dataset from Excel (.xls).

    Dataset structure:
    - Row 0: X1, X2, ..., X23, Y
    - Row 1: Feature descriptions
    - Row 2 onward: Data
    """
    df = pd.read_excel(
        file_path,
        header=0,
        skiprows=[1]
    )
    if "ID" in df.columns:
        df.drop(columns=["ID"], inplace=True)
    target_col = "Y"

    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found. Found columns: {df.columns.tolist()}")

    X = df.drop(columns=[target_col])
    y = df[target_col]
    split_index = int(len(df) * (1 - test_size))

    X_train = X.iloc[:split_index]
    X_test = X.iloc[split_index:]
    y_train = y.iloc[:split_index]
    y_test = y.iloc[split_index:]

    return X_train, X_test, y_train, y_test


