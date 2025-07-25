import pandas as pd
import os
from extract import load_csv  # 🔁 reuse the loader

# This script inspects will serve as a way to inspect  files in any specified directory, loading them into pandas DataFrames and printing basic information about each.
# The goal is to quickly understand the structure and content of the data files and identify any potential issues and what we might need to clean and transform.

DATA_DIR = 'data/csv-files'
dataframes = {}

for filename in os.listdir(DATA_DIR):
    if filename.endswith(".csv"):
        try:
            df = load_csv(filename, folder=DATA_DIR)  # 🔁 reuse the loader
            dataframes[filename] = df

            # Optionally: print more inspection info
            print(f"\n📑 Columns: {df.columns.tolist()}")
            print(f"❓ Nulls:\n{df.isnull().sum()}")
            print(f"📊 Sample data:\n{df.head()}\n")
        except Exception as e:
            print(f" ----- ERROR: Failed to load {filename}: {e}")
