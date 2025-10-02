import requests

url = "https://raw.githubusercontent.com/twbs/bootstrap/main/LICENSE"


try:
    response = requests.get(url)
    response.raise_for_status()
    text_content = response.text

    print("Fetched content (first 200 chars):")
    print("-" * 30)
    print(text_content[:200])
    print("-" * 30)

except requests.exceptions.RequestException as e:
    print(f"Error fetching content: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

