import requests
from bs4 import BeautifulSoup
import datetime

# Get the current system date
current_date = datetime.datetime.now()

# Construct the URL for the Wikipedia page for the current day
url = f"https://en.wikipedia.org/wiki/{current_date.strftime('%B')}_{current_date.strftime('%d')}"

# Send a request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Save the HTML content to a file
with open("response_html", "wb") as f:
    f.write(html_content)

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find the main content section of the page
content_div = soup.find("p", {"class": "mw-empty-elt"})

# Find the first paragraph element within the content section

# Print the text of the first paragraph
print(content_div)
