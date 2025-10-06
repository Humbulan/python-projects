# Import the pandas library, which you just installed
import pandas as pd

# Create a dictionary of data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create a pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame to the console
print("Here is your DataFrame:")
print(df)

