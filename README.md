# OpenAlex2RIS

Send DOIs to the OpenAlex API and receive RIS files in return. These files can be imported into reference managers, research information systems, and more.

![OpenAlex2RIS example output](https://github.com/svidmar/OpenAlex2RIS/blob/9bb1f1b3fc8b09e0cf91054361c854077ec2243d/ris.png)

This project consists of two scripts:

- **ris_from_doi.py**: Send a single DOI to the API and receive a RIS file in return.
- **ris_from_csv.py**: Send a list of DOIs in a CSV file and receive multiple RIS files in return.

## ris_from_doi.py

### Overview

`ris_from_doi.py` is a Python script designed to fetch metadata for academic works using their Digital Object Identifier (DOI) from the OpenAlex database and format this metadata into the RIS (Research Information Systems) file format.

### Dependencies

- Python 3
- requests library

### Key Functions

- `fetch_openalex_metadata_by_doi(doi)`: Fetches metadata for a work by its DOI. Users need to replace `my-email@example.com` with their email when making requests to OpenAlex.
- `reconstruct_abstract_from_inverted_index(inverted_index)`: Reconstructs the abstract of a work from an inverted index, if available.
- `format_ris(metadata)`: Formats the fetched metadata into RIS format using a predefined mapping between OpenAlex types and RIS types.
- `save_ris_file(content, filename="output.ris")`: Saves the formatted RIS content to a file.

### Usage

1. Install the requests library if not already installed: `pip install requests`
2. Run the script and enter the DOI when prompted: `python ris_from_doi.py`
3. The script fetches the metadata, formats it into RIS, saves it to a file named `output.ris`, and prints the content.

## ris_from_csv.py

### Overview

`ris_from_csv.py` is a Python script designed to batch process Digital Object Identifiers (DOIs) from a CSV file, fetch their metadata from the OpenAlex database, and create individual RIS files for each entry.

### Dependencies

- Python 3
- requests library
- csv module
- time module

### Key Features

- Processes a list of DOIs provided in a CSV file.
- Fetches metadata for each DOI using the OpenAlex API.
- Formats the fetched metadata into RIS format.
- Saves each entry as a separate RIS file named after the DOI, with slashes replaced by underscores.

### Usage

1. Ensure the requests library is installed: `pip install requests`.
2. Prepare a CSV file with a list of DOIs, one per line.
3. Modify the script to include the path to your CSV file in the `csv_file_path` variable.
4. Run the script: `python ris_from_csv.py`.
5. The script will process each DOI, creating a corresponding RIS file in the script's directory.

### Important Notes

- The script includes a delay between requests to respect the OpenAlex API rate limits.
- Users need to replace `my-email@example.com` with their email when making requests to OpenAlex for compliance with the API's usage policy.
- Ensure correct formatting of the CSV file to avoid processing errors.
