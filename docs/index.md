# read_datalake_utils_fabric

Utility functions for reading files from Azure Data Lake using Microsoft Fabric notebooks.

## Overview

This package provides helpers for discovering, reading, and combining CSV files stored in Azure Data Lake via `mssparkutils`.

## Included functions

- `get_csv_files(directory_path: str)`
- `read_latest(directory_path: str)`
- `read_and_combine(directory_path: str)`
- `get_top_level_folders(directory_path)`

## Installation

```bash
pip install https://github.com/yxuan1996/read_datalake_utils_fabric/releases/download/Production/data_quality_utils-0.3.5-py3-none-any.whl
```

## Build from source

```bash
python setup.py clean --all
python setup.py bdist_wheel
```

The built wheel file will be located in the `/dist` folder.

## Usage

```python
from read_datalake_utils import get_csv_files, read_latest, read_and_combine

files = get_csv_files("abfss://container@storageaccount.dfs.core.windows.net/data/")
df_latest = read_latest("abfss://container@storageaccount.dfs.core.windows.net/data/")
df_all = read_and_combine("abfss://container@storageaccount.dfs.core.windows.net/data/")
```
