"""
Data preprocessing functions for the project.
Converts raw CSV/JSON into cleaned CSVs for modeling.
"""

import os
import pandas as pd

RAW_DIR = "data/raw/"
PROCESSED_DIR = "data/processed/"
os.makedirs(PROCESSED_DIR, exist_ok=True)


def preprocess():
    """Preprocess the daily rainfall CSV."""
    raw_file = os.path.join(RAW_DIR, "daily_rainfall.csv")
    df = pd.read_csv(raw_file)
    print(f"Original data shape: {df.shape}")

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])
    # Fill missing rainfall values with 0
    df["actual"] = df["actual"].fillna(0)
    # Save processed CSV
    df.to_csv(os.path.join(PROCESSED_DIR, "daily_rainfall.csv"), index=False)
    print("Processed daily_rainfall.csv saved.")
