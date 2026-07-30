"""
Data Ingestion Module
This module is responsible for all tasks related to data ingestion.
Author: Pooja Soni
Project: Retail Data Quality Platform
"""

from dataclasses import dataclass
from pathlib import Path
import pandas as pd

@dataclass
class data_ingestion_files:
    files_found:int
    files_processed:int
    files_rejected:int
    dataframes:pd.DataFrame
    audit:list[dict]
RAW_DATA_FOLDER = Path("data/Raw")


def locate_raw_data_folder() -> Path:
    if not RAW_DATA_FOLDER.exists():
        
        raise FileNotFoundError(f"Raw data folder not found at {RAW_DATA_FOLDER}") 
    return RAW_DATA_FOLDER         
    
def discover_csv_files(raw_folder: Path) -> list(Path):
    csv_files=list(raw_folder.glob("*.csv"))
    return csv_files

def ingest_csv_files(csv_files: list(Path)) -> data_ingestion_files:
    dataframes=[]
    audit=[]
    files_found=len(csv_files)
    files_processed=0
    files_rejected=0
    
    
    for file in csv_files:
        try:
            df=pd.read_csv(file)
            dataframes.append(df)
            files_processed+=1
            audit.append({
                "file_name": file.name,
                "status": "Processed",
                "rows_ingested": len(df),
                "error": None
            })
            
        except Exception as e:
            files_rejected+=1
            audit.append({
                "file_name": file.name,
                "status": "Rejected",
                "rows_ingested": 0,
                "error": str(e)
            })
        
        print("\n========== INGESTION SUMMARY ==========")
    print(f"Files Found      : {files_found}")
    print(f"Files Processed  : {files_processed}")
    print(f"Files Rejected   : {files_rejected}")
    print("=======================================\n")

    return data_ingestion_files(
        files_found=files_found,
        files_processed=files_processed,
        files_rejected=files_rejected,
        dataframes=dataframes,
        audit=audit
    )

def run_data_ingestion():
    raw_folder = locate_raw_data_folder()
    csv_files = discover_csv_files(raw_folder)
    ingestion_summary = ingest_csv_files(csv_files)
    return ingestion_summary