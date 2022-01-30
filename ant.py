from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient

# Define URL with a dynamic web content
url = "https://exploit-db.com"

# Create a ScrapingAntClient instance
client = ScrapingAntClient(token='41df7870b73248c280465778f61fa91e')

# Get the HTML page rendered content
page_content = client.general_request(url).content

# Parse content with BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')
print(soup.find(id="exploits-table").get_text())
t = soup.find('a')

for i in t:
    compare = i.get_attribute("href")
    if ("exploits") in t:
        print(i.text + "\nDL LINK: " + compare.replace("exploits", "download") + "\n")