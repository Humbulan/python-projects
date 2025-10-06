print("=== Python Environment Test ===")
print("Python is working correctly!")
print(f"Current directory: $(pwd)")

# Test pandas
try:
    import pandas as pd
    print("✓ Pandas imported successfully")
except ImportError as e:
    print("✗ Pandas import failed:", e)

# Test basic file operations
import os
print(f"Files in current directory: {len(os.listdir('.'))} files")
for file in os.listdir('.'):
    if file.endswith('.py'):
        print(f" - {file}")
