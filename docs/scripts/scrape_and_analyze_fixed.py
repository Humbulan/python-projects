import requests
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def fetch_periodic_table():
    url = "https://en.wikipedia.org/wiki/List_of_chemical_elements"
    
    # Add headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def analyze_existing_data():
    # Since web scraping might fail, let's analyze the CSV we already have
    print("Analyzing existing periodic table data...")
    try:
        df = pd.read_csv('../data/periodic_table_found.csv')
        print(f"Successfully loaded data with {len(df)} elements")
        
        # Basic analysis
        print(f"Columns available: {df.columns.tolist()}")
        
        if 'Atomic weight' in df.columns:
            print(f"Average atomic weight: {df['Atomic weight'].mean():.2f}")
            print(f"Lightest element: {df.loc[df['Atomic weight'].idxmin(), 'Element']}")
            print(f"Heaviest element: {df.loc[df['Atomic weight'].idxmax(), 'Element']}")
        
        return True
    except Exception as e:
        print(f"Error analyzing existing data: {e}")
        return False

def main():
    print("=== Periodic Table Analysis ===")
    
    # Try web scraping first
    html_content = fetch_periodic_table()
    if html_content:
        print("Successfully fetched data from Wikipedia!")
        # You could add parsing logic here
    else:
        print("Web scraping failed, using existing data file...")
    
    # Analyze the CSV we already have
    analyze_existing_data()

if __name__ == "__main__":
    main()
