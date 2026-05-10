# read_datalake_utils_fabric

Contains utility functions for reading files from Azure Data Lake using MS Fabric Notebooks. 

`read_datalake_utils.py` contains the following functions:

- `get_csv_files(directory_path: str)` - Get list of all CSV files in a directory
- `read_latest(directory_path: str)` - Find most recent CSV file based on modification time
- `read_and_combine(directory_path: str)` - Read and combine all CSV files in a directory

## Building the wheel
`setup.py` contains instructions on how to package the module. 

Run the 2 commands to build the wheel:
```
python setup.py clean --all
python setup.py bdist_wheel
```

Our python wheel file is now located in the `/dist` folder. 
