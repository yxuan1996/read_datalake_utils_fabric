# API Reference

## `get_csv_files(directory_path: str)`

Retrieves all CSV file paths found under a given directory in the Spark filesystem.

- Traverses subdirectories recursively.
- Returns a list of CSV paths.

### Example

```python
files = get_csv_files("abfss://container@storageaccount.dfs.core.windows.net/data/")
```

## `read_latest(directory_path: str)`

Finds the most recent CSV file based on modification time and returns it as a pandas DataFrame.

### Example

```python
df = read_latest("abfss://container@storageaccount.dfs.core.windows.net/data/")
```

## `read_and_combine(directory_path: str)`

Reads and concatenates all CSV files found under a directory into one DataFrame.

### Example

```python
df = read_and_combine("abfss://container@storageaccount.dfs.core.windows.net/data/")
```

## `get_top_level_folders(directory_path)`

Returns all top-level folder paths from a directory in the Spark filesystem.

- Detects folders using `size == 0` from `mssparkutils.fs.ls`.

### Example

```python
folders = get_top_level_folders("abfss://container@storageaccount.dfs.core.windows.net/sap_raw_reports/")
```
