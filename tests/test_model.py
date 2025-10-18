# tests/test_model.py
import os
import sys
import pandas as pd

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
import train_model

PROCESSED_DIR = "data/processed/"


def test_train_model_runs():
    """
    Ensure the model trains without errors and is returned properly.
    """
    # Make sure processed CSV exists
    csv_path = os.path.join(PROCESSED_DIR, "daily_rainfall.csv")
    assert os.path.exists(csv_path), "Processed daily_rainfall.csv missing"

    # Read the CSV to check for NaNs in features
    df = pd.read_csv(csv_path)
    features = ["rfs", "normal", "deviation"]

    # Drop rows with NaN in features
    df_clean = df.dropna(subset=features)

    # If cleaning removed all rows, fail the test
    assert not df_clean.empty, "All rows removed due to NaN in features"

    # Train model on clean data
    model = train_model.train_model(df_clean)  # pass df_clean to the function

    # Check model is returned
    assert model is not None
