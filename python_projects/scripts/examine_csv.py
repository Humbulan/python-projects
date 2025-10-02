import pandas as pd

df = pd.read_csv('../data/periodic_table_found.csv')
print("=== CSV FILE STRUCTURE ===")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"\\nFirst 3 rows:")
print(df.head(3))
print(f"\\nColumn dtypes:")
print(df.dtypes)
