import csv
import requests
import time

# OpenAlex to RIS type mapping
openalex_to_ris_type_mapping = {
    'article': 'JOUR',
    'book-chapter': 'CHAP',
    'book': 'BOOK',
    'dissertation': 'THES',
    'report': 'RPRT',
    'editorial': 'JOUR',
    'letter': 'JOUR',
}

def fetch_openalex_metadata_by_doi(doi):
    """Fetch metadata for a specific work by DOI from OpenAlex. Replace my-email@example.com with your e-mail"""
    url = f"https://api.openalex.org/works?filter=doi:{doi}&mailto=my-email@example.com"
    response = requests.get(url)
    if response.status_code == 200 and response.json()['results']:
        return response.json()['results'][0]
    else:
        print(f"Failed to fetch data for DOI {doi}. Please check the DOI and your internet connection.")
        return None

def reconstruct_abstract_from_inverted_index(inverted_index):
    """Reconstruct abstract text from an inverted index if available."""
    if not inverted_index or not isinstance(inverted_index, dict):
        return ""
    
    word_positions = [(word, pos) for word, positions in inverted_index.items() for pos in positions]
    sorted_word_positions = sorted(word_positions, key=lambda x: x[1])
    
    words_in_order = [word for word, pos in sorted_word_positions]
    reconstructed_abstract = " ".join(words_in_order)
    return reconstructed_abstract

def format_ris(metadata):
    """Format metadata into RIS file content."""
    ris_type = openalex_to_ris_type_mapping.get(metadata.get('type', ''), 'GEN')
    ris_content = f"TY  - {ris_type}\n"
    ris_content += f"T1  - {metadata.get('title', 'No title available')}\n"

def save_ris_file(content, filename):
    """Save RIS content to a file."""
    with open(filename, "w") as file:
        file.write(content)
    print(f"Saved RIS file: {filename}")

def main(csv_file_path):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        last_request_time = time.time() - 0.1  # Initialize to allow immediate first request
        for row in reader:
            current_time = time.time()
            time_since_last_request = current_time - last_request_time
            
            # Ensure at least 0.1 second delay between requests to respect API limits
            if time_since_last_request < 0.1:
                time.sleep(0.1 - time_since_last_request)
            
            doi = row[0]
            metadata = fetch_openalex_metadata_by_doi(doi)
            if metadata:
                ris_content = format_ris(metadata)
                filename = f"{doi.replace('/', '_')}.ris"
                save_ris_file(ris_content, filename)
            
            last_request_time = time.time()

if __name__ == "__main__":
    csv_file_path = "/Users/something/somefolder/dois.csv"  # Update this to the path of your CSV file
    main(csv_file_path)
