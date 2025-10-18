"""
Helper utility functions for the project.
"""

import pandas as pd


def load_csv(file_path):
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(file_path)


def safe_divide(a, b):
    """Safely divide a by b, return 0 if b is zero."""
    if b == 0:
        return 0
    return a / b
