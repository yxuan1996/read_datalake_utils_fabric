# Utility Functions with mssparkutils

"""
This module contains several utility functions for reading data from data lake.

The module contains the following functions:

- `get_csv_files(directory_path: str)` - Get list of all CSV files in a directory
- `read_latest(directory_path: str)` - Find most recent CSV file based on modification time
- `read_and_combine(directory_path: str)` - Read and combine all CSV files in a directory
"""

from IPython.core.getipython import get_ipython
mssparkutils = get_ipython().user_ns.get("mssparkutils")

from typing import List
import pandas as pd

# Get list of all CSV files in a directory
def get_csv_files(directory_path: str) -> List[str]:
  """
    Recursively retrieves the list of all CSV file paths within a given directory in the 
    Azure Synapse/Spark filesystem.

    This function traverses subdirectories if encountered (indicated by zero file size),
    and collects file paths ending with `.csv`.

    Args:
        directory_path (str): The root directory path in the Spark filesystem to search.

    Returns:
        List[str]: A list containing the full paths of CSV files found.

    Example:
        >>> files = get_csv_files("abfss://container@storageaccount.dfs.core.windows.net/data/")
        >>> print(files)
        [
            "abfss://container@storageaccount.dfs.core.windows.net/data/file1.csv",
            "abfss://container@storageaccount.dfs.core.windows.net/data/subdir/file2.csv"
        ]
  """
  csv_files = []
  newcsv_files = []
  files_to_treat = mssparkutils.fs.ls(directory_path)
  while files_to_treat:
    file_to_treat = files_to_treat.pop(0)
    path = file_to_treat.path
    size = file_to_treat.size
    if size==0:
      files_to_treat += mssparkutils.fs.ls(path)
    elif path.endswith(".csv"):
            csv_files.append(path)
      
  return csv_files

# Find most recent CSV file based on modification time
def read_latest(directory_path: str) -> pd.DataFrame:
    """
    Reads the most recent CSV file from a directory based on its modification time.

    This function traverses subdirectories, collects all CSV files, 
    determines the latest one, and loads it into a pandas DataFrame.

    Args:
        directory_path (str): The directory path in the Spark filesystem.

    Returns:
        pd.DataFrame: DataFrame containing the contents of the latest CSV file.

    Example:
        >>> df = read_latest("abfss://container@storageaccount.dfs.core.windows.net/data/")
        Reading most recent file: sales_data.csv
        abfss://container@storageaccount.dfs.core.windows.net/data/sales_data.csv
        >>> df.head()
           id   amount   date
        0   1   200.50  2025-08-01
        1   2   150.00  2025-08-02
    """
    csv_files = []
    newcsv_files = []
    files_to_treat = list(mssparkutils.fs.ls(directory_path))
    while files_to_treat:
        file_to_treat = files_to_treat.pop(0)
        path = file_to_treat.path
        size = file_to_treat.size
        if size==0:
            files_to_treat.extend(mssparkutils.fs.ls(path))
        elif path.endswith(".csv"):
            csv_files.append(file_to_treat)
    

    # Find most recent file based on modification time
    most_recent = max(csv_files, key=lambda f: f.modifyTime)

    print(f"Reading most recent file: {most_recent.name}")
    print(most_recent.path)
    df = pd.read_csv(most_recent.path)
    return df

# Read and combine all CSV files in a directory
def read_and_combine(directory_path: str) -> pd.DataFrame:
    """
    Reads and concatenates all CSV files within a given directory (and its subdirectories).

    This function searches for CSV files recursively and merges them into a single DataFrame.

    Args:
        directory_path (str): The directory path in the Spark filesystem.

    Returns:
        pd.DataFrame: A DataFrame containing the combined data from all CSV files.

    Example:
        >>> df = read_and_combine("abfss://container@storageaccount.dfs.core.windows.net/data/")
        >>> df.shape
        (5000, 10)  # Combined rows and columns from all CSV files
    """
    combined_df = pd.DataFrame()
    csv_files = []
    newcsv_files = []
    files_to_treat = list(mssparkutils.fs.ls(directory_path))
    while files_to_treat:
        file_to_treat = files_to_treat.pop(0)
        path = file_to_treat.path
        size = file_to_treat.size
        if size==0:
            files_to_treat.extend(mssparkutils.fs.ls(path))
        elif path.endswith(".csv"):
            csv_files.append(file_to_treat)
    
    for a in csv_files:
        df = pd.read_csv(a.path)
        combined_df = pd.concat([combined_df, df],ignore_index=True)
    return combined_df

def get_top_level_folders(directory_path):
    """
    Retrieve a list of top-level folders from a given directory in Azure Fabric/Databricks 
    using `mssparkutils.fs.ls`.

    A folder is identified as an entry with `size == 0` (the way `mssparkutils` 
    indicates directories).

    Args:
        directory_path (str): 
            The path to the directory in the mounted filesystem where the 
            folders should be retrieved.

    Returns:
        list[str]: 
            A list of folder paths (strings) representing the top-level folders 
            found in the specified directory.

    Example:
        >>> get_top_level_folders("abfss://raw@accountname.dfs.core.windows.net/sap_raw_reports/")
        ['abfss://raw@accountname.dfs.core.windows.net/sap_raw_reports/folder1/',
         'abfss://raw@accountname.dfs.core.windows.net/sap_raw_reports/folder2/']
    """
    folders = []
    files_to_treat = mssparkutils.fs.ls(directory_path)
    while files_to_treat:
        file_to_treat = files_to_treat.pop(0)
        path = file_to_treat.path
        size = file_to_treat.size
        if size == 0:
            folders.append(path)
    return folders
