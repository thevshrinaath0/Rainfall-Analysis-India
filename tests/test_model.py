import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
import train_model

PROCESSED_DIR = "data/processed/"


def test_train_model_runs():
    # Make sure processed CSV exists
    path = os.path.join(PROCESSED_DIR, "daily_rainfall.csv")
    assert os.path.exists(path), "Processed daily_rainfall.csv missing"

    # Run training script
    model = train_model.train_model()
    assert model is not None
