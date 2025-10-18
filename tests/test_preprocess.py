import os
import sys
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))
import preprocess

PROCESSED_DIR = "data/processed/"


def test_rainfall_csv_created():
    path = preprocess.preprocess_rainfall()
    assert os.path.exists(path), "Processed daily_rainfall.csv missing"


def test_rainfall_csv_not_empty():
    path = os.path.join(PROCESSED_DIR, "daily_rainfall.csv")
    df = pd.read_csv(path)
    assert not df.empty, "daily_rainfall.csv is empty"
