import requests

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
    """Fetch metadata for a specific work by DOI from OpenAlex. Replace my-email@example.com with your e-mail """
    url = f"https://api.openalex.org/works?filter=doi:{doi}&mailto=my-email@example.com"
    response = requests.get(url)
    if response.status_code == 200 and response.json()['results']:
        return response.json()['results'][0]  # Assuming the first result is the correct one as a DOI is expected to be unique
    else:
        print("Failed to fetch data. Please check the DOI and your internet connection.")
        return None

def reconstruct_abstract_from_inverted_index(inverted_index):
    """Reconstruct abstract text from an inverted index if available."""
    if not inverted_index or not isinstance(inverted_index, dict):
        return ""  # Return an empty string if no abstract is provided or structure is unexpected
    
    word_positions = [(word, pos) for word, positions in inverted_index.items() for pos in positions]
    sorted_word_positions = sorted(word_positions, key=lambda x: x[1])
    
    words_in_order = [word for word, pos in sorted_word_positions]
    reconstructed_abstract = " ".join(words_in_order)
    return reconstructed_abstract

def format_ris(metadata):
    """Format metadata into RIS file content."""
    # Determine the RIS type based on the OpenAlex type
    ris_type = openalex_to_ris_type_mapping.get(metadata.get('type', ''), 'GEN')  # Default to 'GEN' if not found
    ris_content = f"TY  - {ris_type}\n"
    ris_content += f"T1  - {metadata.get('title', 'No title available')}\n"
    
    # Ensure 'primary_location' exists and is a dictionary, then access 'source' safely
    primary_location = metadata.get('primary_location', {})
    source = primary_location.get('source', {}) if isinstance(primary_location, dict) else None
    
    # Check if 'source' is a dictionary before attempting to access its properties
    if isinstance(source, dict):
        journal_name = source.get('display_name', '')
        if journal_name:
            ris_content += f"T2  - {journal_name}\n"
        
        issn_l = source.get('issn_l', '')
        if issn_l:
            ris_content += f"SN  - {issn_l}\n"
        else:
            # Handle the case where 'issn_l' is not present but 'issn' might be
            issns = source.get('issn', [])
            if issns:
                ris_content += f"SN  - {issns[0]}\n"
    else:
        # Handle cases where 'source' is None or not a dictionary
        print("Warning: 'source' information is missing or invalid in metadata.")

    
    for author in metadata.get('authorships', []):
        author_name = author.get('author', {}).get('display_name', 'No author name')
        ris_content += f"A1  - {author_name}\n"
    
    if 'publication_year' in metadata:
        ris_content += f"PY  - {metadata['publication_year']}\n"
    
    if 'biblio' in metadata:
        biblio = metadata.get('biblio', {})
        if 'volume' in biblio:
            ris_content += f"VL  - {biblio.get('volume', '')}\n"
        if 'issue' in biblio:
            ris_content += f"IS  - {biblio.get('issue', '')}\n"
        if 'first_page' in biblio and 'last_page' in biblio:
            ris_content += f"SP  - {biblio.get('first_page', '')}\n"
            ris_content += f"EP  - {biblio.get('last_page', '')}\n"
    
    if 'doi' in metadata:
        ris_content += f"DO  - {metadata.get('doi', '')}\n"
    
    if 'language' in metadata:
        ris_content += f"LA  - {metadata.get('language', '')}\n"
    
    keywords = metadata.get('keywords', [])
    for keyword in keywords:
        keyword_text = keyword.get('keyword', '')
        if keyword_text:
            ris_content += f"KW  - {keyword_text}\n"
    
    oa_url = metadata.get('open_access', {}).get('oa_url', '')
    if oa_url:
        ris_content += f"L2  - {oa_url}\n"
    
    if 'abstract_inverted_index' in metadata:
        abstract = reconstruct_abstract_from_inverted_index(metadata['abstract_inverted_index'])
        if abstract:
            ris_content += f"AB  - {abstract}\n"
    
    ris_content += "ER  - \n"
    return ris_content

def save_ris_file(content, filename="output.ris"):
    """Save RIS content to a file and print the content."""
    with open(filename, "w") as file:
        file.write(content)
    print(f"Saved RIS file: {filename}")
    return content

def main():
    doi = input("Enter the DOI: ")
    metadata = fetch_openalex_metadata_by_doi(doi)
    if metadata:
        ris_content = format_ris(metadata)
        print(save_ris_file(ris_content))  # Save and print the content of the RIS file
    else:
        print("No metadata found for the given DOI.")

if __name__ == "__main__":
    main()
