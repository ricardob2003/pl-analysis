import pandas as pd
import os

def load_csv(file_name, folder='data/raw'):
    """
    Load data from a CSV file.

    Args:
        file_name (str): The name of the CSV file.
        folder (str): The folder where the CSV file is located.

    Returns:
        pd.DataFrame: A DataFrame containing the loaded data.
    """
    file_path = os.path.join(folder, file_name)
    try:
        df = pd.read_csv(file_path, encoding='utf-8', dtype=str)
        print(f" Loaded '{file_name}' with {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except FileNotFoundError:
        print(f" File not found: {file_path}")
        return None
    except Exception as e:
        print(f" Failed to load {file_name}: {e}")
        return None

def run_extraction():
    """
    Run the extraction process for all CSV files in the folder.
    """
    folder = 'data/raw'
    if not os.path.exists(folder):
        print(f" Folder does not exist: {folder}")
        return

    print(f"\n📥 Extracting files from: {folder}\n")

    for file_name in os.listdir(folder):
        if file_name.endswith('.csv'):
            load_csv(file_name, folder=folder)

    print("\n Extraction test complete.\n")

if __name__ == "__main__":
    run_extraction()
