import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the data
df = pd.read_csv('../data/periodic_table_found.csv')

print("=== WORKING PERIODIC TABLE ANALYSIS ===")
print(f"Dataset shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")

# Display the actual data structure
print("\nFirst 10 rows:")
print(df.head(10))

# Basic info about the dataset
print(f"\nBasic Info:")
print(f"Number of elements: {len(df)}")
print(f"Number of columns: {len(df.columns)}")

# Check for numeric columns and analyze them
numeric_columns = df.select_dtypes(include=['number']).columns
print(f"\nNumeric columns: {list(numeric_columns)}")

if len(numeric_columns) > 0:
    print(f"\nStatistical Summary:")
    print(df[numeric_columns].describe())

# Create a simple visualization if we have numeric data
if len(numeric_columns) >= 2:
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(df[numeric_columns[0]], df[numeric_columns[1]], alpha=0.7)
        plt.title(f'{numeric_columns[1]} vs {numeric_columns[0]}')
        plt.xlabel(numeric_columns[0])
        plt.ylabel(numeric_columns[1])
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig('../output/elements_analysis.png', dpi=150, bbox_inches='tight')
        print(f"\nSaved visualization to ../output/elements_analysis.png")
    except Exception as e:
        print(f"Could not create visualization: {e}")

print("\n✅ Analysis completed successfully!")
