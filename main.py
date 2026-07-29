from src.ingestion import locate_raw_data_folder, discover_csv_files
raw_folder = locate_raw_data_folder()
csv_files = discover_csv_files(raw_folder)
print(f"Discovered CSV files: {csv_files}")
