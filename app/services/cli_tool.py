import requests
from PyPDF2 import PdfReader
import argparse

# Set FastAPI base URL
BASE_URL = "http://127.0.0.1:8000"  # Ensure your FastAPI server is running

def extract_pdf_data(pdf_path):
    """Extract text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def call_api(endpoint, payload):
    """Send a POST request to the FastAPI endpoint."""
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

def main():
    parser = argparse.ArgumentParser(description="Process a PDF file and interact with APIs.")
    parser.add_argument("pdf_file", help="Path to the PDF file.")
    args = parser.parse_args()

    # Extract data from the PDF
    pdf_path = args.pdf_file
    text = extract_pdf_data(pdf_path)
    lines = text.split("\n")

    if len(lines) < 2:
        print("Error: The PDF must have at least two lines (year and string).")
        return

    try:
        year = int(lines[0])  # First line is the year
        string = lines[1]  # Second line is the string
    except ValueError:
        print("Error: The first line of the PDF must be a valid year.")
        return

    print(f"Extracted Year: {year}")
    print(f"Extracted String: {string}")

    # Call APIs
    print("\nCalling Leap Year API...")
    leap_year_result = call_api("/check-leap-year/", {"year": year})
    print(f"Result: {leap_year_result}")

    print("\nCalling Prime Year API...")
    prime_year_result = call_api("/check-prime/", {"year": year})
    print(f"Result: {prime_year_result}")

    print("\nCalling String Split and Join API...")
    string_split_join_result = call_api("/string-split-join/", {"string": string})
    print(f"Result: {string_split_join_result}")

if __name__ == "__main__":
    main()
