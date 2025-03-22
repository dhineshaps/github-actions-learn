import requests
from bs4 import BeautifulSoup
#import pandas as pd
import sys
import time

# URL of the website
url = "https://www.5paisa.com/sectors/all"

#url = "https://www.5paisa.com/stocks/sector/5g"

base_url = "https://www.5paisa.com"

fil = open("url_links_sector.txt", "w")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


response = requests.get(url, headers=headers)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

print(response.status_code)

table = soup.find("table", {"id": "sortableTable"})  # Get the table with the given id

if table:
    tbody = table.find("tbody")  # Find tbody inside the table
    if tbody:
        for row in tbody.find_all("tr"):
            link = row.find('a')
            if link:
                relative_url = link.get('href') 
                full_url = base_url + relative_url
                print(full_url)
                fil.write(full_url+"\n")  
    else:
        print("No tbody found in the table")
fil.close()
