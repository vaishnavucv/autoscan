# Link Extractor

This Python script uses BeautifulSoup to extract all the links from a user-specified webpage and saves them to a text file. The file is named based on the domain name of the input URL.

## Requirements

- Python 3.x
- requests library
- BeautifulSoup library

## Installation

1. Clone the repository:
    ```sh
    wget https://raw.githubusercontent.com/vaishnavucv/autoscan/main/links-extractor/extractor.py
    ```

2. Change Chmod:
    ```sh
    chmod +x extractor.py
    ```

3. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python3 extractor.py
    ```

2. Enter the URL of the webpage when prompted.

3. The script will print the extracted links to the terminal and save them to a text file named based on the domain name of the input URL.

## Example

```sh
$ python3 extractor.py
Enter the URL of the webpage: https://example.com
Extracted Links:
https://example.com/about
https://example.com/contact
...
Links saved to example.com_links.txt

