import requests
from bs4 import BeautifulSoup

def get_all_links(url):
    # Send a GET request
    response = requests.get(url)
    #print(response)
    response.raise_for_status()  # Raise an exception if the status code isn't 200 OK

    # Parse the document
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)

    # Find all <a> tags with href attributes
    links = [a['href'] for a in soup.find_all('a', href=True)]

    return links

# Use the function and print the links
links = get_all_links('https://www.youtube.com')
print(links)
