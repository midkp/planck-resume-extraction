import sys
import os
import csv
import PyPDF2

def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file."""
    try:
        with open(pdf_file, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text.strip()
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def extract_values_from_csv(csv_file):
    """Extract values from a CSV file."""
    try:
        with open(csv_file, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            # Flatten the rows into a single list of values
            values = [item for sublist in rows for item in sublist]
            return values
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cli_tool.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    if file_path.lower().endswith(".pdf"):
        # Handle PDF file
        print("Importing string from PDF")
        extracted_text = extract_text_from_pdf(file_path)
        if extracted_text:
            print(f"Extracted text from PDF: {extracted_text}")
        else:
            print("No text found in the PDF.")
    elif file_path.lower().endswith(".csv"):
        # Handle CSV file
        print("Importing values from CSV")
        extracted_values = extract_values_from_csv(file_path)
        if extracted_values:
            # Format output similar to PDF result
            print(f"Extracted values from CSV: {' | '.join(extracted_values)}")
        else:
            print("No values found in the CSV.")
    else:
        print(f"Unsupported file format: {file_path}. Please provide a .pdf or .csv file.")
