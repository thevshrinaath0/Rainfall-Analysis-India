"""
train_model.py

Contains functions to train a linear regression model on rainfall data.
"""

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

PROCESSED_DIR = "data/processed"


def train_model(df=None):
    """
    Train a simple linear regression model on the rainfall data.

    Args:
        df (pd.DataFrame, optional): Preprocessed DataFrame. If None, reads from CSV.

    Returns:
        LinearRegression: Trained model.
    """
    if df is None:
        df = pd.read_csv(os.path.join(PROCESSED_DIR, "daily_rainfall.csv"))

    # Feature selection
    features = ["rfs", "normal", "deviation"]
    df = df.dropna(subset=features)
    x_data = df[features]
    y_data = df["actual"]

    # Split into train/test
    x_train, _, y_train, _ = train_test_split(
        x_data, y_data, test_size=0.2, random_state=42
    )

    # Train model
    model = LinearRegression()
    model.fit(x_train, y_train)

    return model
