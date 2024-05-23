# Import the necessary libraries
import requests  # To make HTTP requests to fetch the webpage
from bs4 import BeautifulSoup  # To parse the HTML content
from urllib.parse import urlparse  # To parse the URL and extract the domain name

# Get the URL from the user
url = input("Enter the URL of the webpage: ")

# Make an HTTP GET request to fetch the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the anchor tags in the webpage
    links = soup.find_all('a')

    # Extract the URLs from the anchor tags
    urls = [link.get('href') for link in links if link.get('href')]

    # Print the URLs to the terminal
    print("Extracted Links:")
    for url in urls:
        print(url)

    # Parse the domain name from the input URL
    domain = urlparse(url).netloc

    # Create a filename based on the domain name
    filename = f"{domain}_links.txt"

    # Save the URLs to a text file
    with open(filename, 'w') as file:
        for url in urls:
            file.write(url + '\n')

    print(f"Links saved to {filename}")

else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
