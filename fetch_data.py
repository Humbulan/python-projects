import pandas as pd
import requests
import io
import matplotlib.pyplot as plt # Needed for plotting

def main():
    print("Hello, SK RNX Python World!")

    # Define the URL for your data.
    # This URL is a common source for COVID-19 time series data.
    # If your data is from a different source, update this URL.
    url = "https://raw.githubusercontent.com/datasets/covid-19/main/data/time-series-19-covid-combined.csv"

    data = None # Initialize data to None

    try:
        print(f"Attempting to fetch data from: {url}")
        response = requests.get(url)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        print("Data fetched successfully!")

        # Read the CSV data directly into a pandas DataFrame
        data = pd.read_csv(io.StringIO(response.text))
        print("Data loaded into DataFrame.")
        # Optional: Print a description of the data to verify it loaded correctly
        # print(data.describe())
        # print(data.head()) # Shows the first few rows of the DataFrame

        # --- Data Processing ---
        # Convert 'Date' column to datetime objects
        # Ensure the 'Date' column exists in your CSV data
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'])
            print("Date column converted to datetime objects.")
        else:
            print("Warning: 'Date' column not found in the data. Please check your CSV file.")
            return # Exit if essential column is missing

        # Aggregate global confirmed cases per day
        # Ensure 'Confirmed' column exists for aggregation
        if 'Confirmed' in data.columns:
            daily_global_cases = data.groupby('Date')['Confirmed'].sum()
            print("Daily global confirmed cases aggregated.")
        else:
            print("Warning: 'Confirmed' column not found in the data. Cannot aggregate cases.")
            return # Exit if essential column is missing

        # --- Plotting ---
        print("\nPlotting Global Confirmed Cases over Time...")
        plt.figure(figsize=(12, 6)) # Adjust figure size for better readability
        plt.plot(daily_global_cases.index, daily_global_cases, marker='o', linestyle='-') # Added marker and linestyle for clarity
        plt.title('Global Confirmed COVID-19 Cases Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Confirmed Cases')
        plt.grid(True)
        plt.tight_layout() # Adjust layout to prevent labels from overlapping

        # Save the plot to a file instead of trying to display a GUI window
        output_filename = "covid_cases_plot.png"
        plt.savefig(output_filename)
        print(f"Plot saved as {output_filename}")

        # plt.show() # This line is commented out as it won't display visibly in your current setup
        # print("Plot displayed (if graphical backend available).")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Check the URL or your internet connection.")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err} - Check your internet connection.")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err} - Request took too long.")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred during the request: {req_err}")
    except KeyError as ke:
        print(f"KeyError: Column missing. Check if 'Date' or 'Confirmed' columns exist in your CSV. Error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# This ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()

