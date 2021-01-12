import requests
from bs4 import BeautifulSoup
import csv

def cmpny_name_link():
    url = "https://www.moneycontrol.com/stocks/marketstats/nsemact1/index.php?index=FNO"

    response = requests.get(url)
    mycontent = response.content
   
    soup = BeautifulSoup(mycontent,'html.parser')

    cmpny_links_names = {}
    result = soup.find_all("td",class_ = "PR")
    for r in result:
        count += 1
        cmpny_links_names[r.find("a").text] = r.find("a")["href"]
    return cmpny_links_names

print(cmpny_name_link())
