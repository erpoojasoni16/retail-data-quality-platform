from src.ingestion import locate_raw_data_folder, discover_csv_files, read_csv_file
raw_folder = locate_raw_data_folder()
csv_files = discover_csv_files(raw_folder)
if not csv_files:
    print("No CSV files found in the raw data folder." )
    print("pipeline finished")

print(f"{len(csv_files)} CSV files found in the raw data folder.")
for file in csv_files:
    try:
        df=read_csv_file(file)
        print(f'File_name:{file.name}')
        print(f'Number of rows: {df.shape[0]}')
        print(f'Number of columns: {df.shape[1]}')
        print("-" * 50)
    except Exception as error:
        print(f"ERROR : Unable to read {file.name}")
        print(f"Reason: {error}")
        print("-" * 50)
        
