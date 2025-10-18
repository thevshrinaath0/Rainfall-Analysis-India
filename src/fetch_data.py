"""
Data fetching functions.
Fetches raw data files from online sources or local placeholders.
"""

import os

RAW_DIR = "data/raw/"
os.makedirs(RAW_DIR, exist_ok=True)
