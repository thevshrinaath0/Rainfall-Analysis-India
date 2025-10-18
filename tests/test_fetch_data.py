import os
import pytest

RAW_DIR = "data/raw/"


def test_rainfall_csv_exists():
    path = os.path.join(RAW_DIR, "daily_rainfall.csv")
    assert os.path.exists(path), "daily_rainfall.csv does not exist in raw folder"
