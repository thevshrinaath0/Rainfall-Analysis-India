"""
Train ML model for rainfall prediction.
"""

import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import joblib

PROCESSED_DIR = "data/processed/"
MODEL_PATH = os.path.join(PROCESSED_DIR, "rainfall_model.pkl")


def train_model():
    """Train a simple linear regression model on the rainfall data."""
    df = pd.read_csv(os.path.join(PROCESSED_DIR, "daily_rainfall.csv"))

    # Feature selection
    features = ["rfs", "normal", "deviation"]
    x_data = df[features]
    y_data = df["actual"]

    # Split into train/test
    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=0.2, random_state=42
    )

    # Train model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Evaluate
    score = r2_score(y_test, model.predict(x_test))
    print(f"Model trained. R^2 score: {score:.2f}")

    # Save model
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved: {MODEL_PATH}")

    return model
