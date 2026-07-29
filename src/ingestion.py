"""
Data Ingestion Module

This module is responsible for discovering and loading
CSV files from the raw data directory.

Author: Pooja Soni
Project: Retail Data Quality Platform
"""


from pathlib import Path
import pandas as pd
RAW_DATA_FOLDER = Path("data/Raw")

def locate_raw_data_folder() -> Path:
    if not RAW_DATA_FOLDER.exists():
        raise FileNotFoundError(f"Raw data folder not found at {RAW_DATA_FOLDER}") 
    return RAW_DATA_FOLDER         
    
def discover_csv_files(raw_folder: Path) -> list(Path):
    csv_files=list(raw_folder.glob("*.csv"))
    return csv_files
    

    
    
    