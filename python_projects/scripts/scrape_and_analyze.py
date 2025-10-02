import requests
import pandas as pd

# The URL of the page we want to scrape
url = "https://en.wikipedia.org/wiki/List_of_chemical_elements"

# Send a GET request to the URL
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
    exit()

# Use pandas to read all tables on the page.
try:
    dfs = pd.read_html(response.text)
    
    if not dfs:
        print("Could not find any tables on the page.")
        exit()

    # Find the periodic table by its content. We'll look for the element 'He'
    periodic_table_df = None
    for df in dfs:
        # We need to make sure we don't get an error on non-string data
        df_as_string = df.to_string()
        if ' He ' in df_as_string: # Look for the string ' He ' with spaces
            periodic_table_df = df
            break
    
    if periodic_table_df is None:
        print("Could not find a table that looks like the periodic table.")
        print("Printing the first few tables for inspection:")
        for i, df in enumerate(dfs[:3]):
            print(f"\n--- Table {i+1} ---")
            print(df.head())
        exit()

    # The table is found! Now let's print the entire table.
    print("Success! Found the periodic table.")
    print("Here is the raw DataFrame before any cleanup:")
    print(periodic_table_df)
    
    # You can now save or analyze this DataFrame.
    periodic_table_df.to_csv('periodic_table_found.csv', index=False)
    print("\nDataFrame saved to 'periodic_table_found.csv'")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

