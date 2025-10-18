"""
preprocess.py

Contains functions to preprocess rainfall data in India.
"""

import os
import pandas as pd

PROCESSED_DIR = "data/processed"


def preprocess():
    """
    Preprocess raw rainfall data and save as CSV.

    Returns:
        str: Path to the processed CSV file.
    """
    os.makedirs(PROCESSED_DIR, exist_ok=True)

    # Load raw data
    raw_path = "data/raw/daily_rainfall.csv"
    df = pd.read_csv(raw_path)

    print(f"Original data shape: {df.shape}")

    # Example preprocessing (you can add more)
    df["deviation"] = df["actual"] - df["normal"]

    processed_path = os.path.join(PROCESSED_DIR, "daily_rainfall.csv")
    df.to_csv(processed_path, index=False)
    print("Processed daily_rainfall.csv saved.")

    return processed_path
