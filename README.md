# OpenAlex2RIS
<br>
Send DOI's to the OpenAlex API and get RIS files in return, which can be imported to reference managers, research information systems etc. 
<br>
<br>

![alt text](https://github.com/svidmar/OpenAlex2RIS/blob/9bb1f1b3fc8b09e0cf91054361c854077ec2243d/ris.png)
<br>
<br>

Consists of two scripts:
<br>
ris_from_doi: Send a single DOI to the API and get a RIS file in return
<br>
ris_from_csv: Send a list of DOIs in a csv and get x RIS files in return


# ris_from_doi.py
Overview:
ris_from_doi.py is a Python script designed to fetch metadata for academic works using their Digital Object Identifier (DOI) from the OpenAlex database and format this metadata into RIS (Research Information Systems) file format.

## Dependencies:

  Python 3
  requests library

## Key Functions:

fetch_openalex_metadata_by_doi(doi): Fetches metadata for a work by its DOI. Users need to replace my-email@example.com with their email when making requests to OpenAlex.

reconstruct_abstract_from_inverted_index(inverted_index): Reconstructs the abstract of a work from an inverted index if available.

format_ris(metadata): Formats the fetched metadata into RIS format. It uses a predefined mapping between OpenAlex types and RIS types.

save_ris_file(content, filename="output.ris"): Saves the formatted RIS content to a file.

## Usage:

Install the requests library if not already installed: pip install requests
Run the script and enter the DOI when prompted: python ris_from_doi.py
The script fetches the metadata, formats it into RIS, saves it to a file named output.ris, and prints the content.

<br>
<br>

# ris_from_csv.py.

## Overview:
ris_from_csv.py is a Python script designed to batch process Digital Object Identifiers (DOIs) from a CSV file, fetch their metadata from the OpenAlex database, and create individual RIS (Research Information Systems) files for each entry. 

## Dependencies:

  Python 3
  requests library
  csv module
  time module

## Key Features:

Processes a list of DOIs provided in a CSV file.
Fetches metadata for each DOI using the OpenAlex API.
Formats the fetched metadata into RIS format.
Saves each entry as a separate RIS file named after the DOI, with slashes replaced by underscores.

## Usage:

Ensure the requests library is installed: pip install requests.
Prepare a CSV file with a list of DOIs, one per line.
Modify the script to include the path to your CSV file in the csv_file_path variable.
Run the script: python ris_from_csv.py.
The script will process each DOI, creating a corresponding RIS file in the script's directory.

## Important Notes:

The script includes a delay between requests to respect the OpenAlex API rate limits.
Users need to replace my-email@example.com with their email when making requests to OpenAlex for compliance with the API's usage policy.
Ensure correct formatting of the CSV file to avoid processing errors.
