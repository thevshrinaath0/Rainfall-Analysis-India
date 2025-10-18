"""
Prediction functions using trained model.
"""

import os
import joblib
import pandas as pd

PROCESSED_DIR = "data/processed/"
MODEL_PATH = os.path.join(PROCESSED_DIR, "rainfall_model.pkl")


def predict_rainfall(new_data: pd.DataFrame):
    """
    Predict rainfall using the trained model.

    Args:
        new_data (pd.DataFrame): DataFrame containing features ['rfs', 'normal', 'deviation']

    Returns:
        pd.Series: Predicted rainfall values
    """
    model = joblib.load(MODEL_PATH)
    predictions = model.predict(new_data)
    return predictions
