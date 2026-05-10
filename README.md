# read_datalake_utils_fabric

Contains utility functions for reading files from Azure Data Lake using MS Fabric Notebooks. 

`read_datalake_utils.py` contains the following functions:

- `get_csv_files(directory_path: str)` - Get list of all CSV files in a directory
- `read_latest(directory_path: str)` - Find most recent CSV file based on modification time
- `read_and_combine(directory_path: str)` - Read and combine all CSV files in a directory

## Download the latest release
```
pip install https://github.com/yxuan1996/read_datalake_utils_fabric/releases/download/Production/read_datalake_utils-0.2.0-py3-none-any.whl
```

## View Documentation
[Documentation](https://yxuan1996.github.io/read_datalake_utils_fabric/)

## Building the wheel
`setup.py` contains instructions on how to package the module. 

Run the 2 commands to build the wheel:
```
python setup.py clean --all
python setup.py bdist_wheel
```

Our python wheel file is now located in the `/dist` folder. 
