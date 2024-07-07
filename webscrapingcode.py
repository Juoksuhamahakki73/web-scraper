import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://www.python.org'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful 
if response.status_code == 200:
    #Parse the HTML content 
    soup = BeautifulSoup(response.content, 'html.parser')

    #Find the data you want to scrape (e.g., headlines)
    headlines = soup.find_all('h1') #Example: Finding all <h1> tags

    # Open a file to write the scraped data
    with open('headlines.txt', 'w') as file:
        for headline in headlines:
            file.write(headline.get_text() + '\n')

        print('Scraping completed. Data saved to headlines.txt')
else:
    print('Failed to retrieve the webpage. Status code:{}'.format(response.status_code))      
