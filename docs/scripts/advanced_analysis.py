import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv('../data/periodic_table_found.csv')

print("=== Advanced Periodic Table Analysis ===")
print(f"Dataset shape: {df.shape}")

# Display basic info
print("\nFirst 5 elements:")
print(df[['Element', 'Atomic weight']].head())

# Statistical summary
if 'Atomic weight' in df.columns:
    print(f"\nAtomic Weight Statistics:")
    print(f"Mean: {df['Atomic weight'].mean():.2f}")
    print(f"Median: {df['Atomic weight'].median():.2f}")
    print(f"Min: {df['Atomic weight'].min():.2f}")
    print(f"Max: {df['Atomic weight'].max():.2f}")

# Group analysis
if 'Group' in df.columns:
    print(f"\nElements by Group:")
    group_counts = df['Group'].value_counts().sort_index()
    for group, count in group_counts.items():
        print(f"Group {group}: {count} elements")

# Create a simple visualization
if 'Atomic weight' in df.columns:
    plt.figure(figsize=(12, 6))
    plt.plot(range(1, len(df) + 1), df['Atomic weight'], marker='o', linewidth=2, markersize=4)
    plt.title('Atomic Weights of Elements')
    plt.xlabel('Element Number')
    plt.ylabel('Atomic Weight')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../output/atomic_weights_plot.png', dpi=150, bbox_inches='tight')
    print(f"\nSaved visualization to ../output/atomic_weights_plot.png")

print("\nAnalysis complete!")
