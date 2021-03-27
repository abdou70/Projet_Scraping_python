import requests
from bs4 import BeautifulSoup

url = 'https://www.samanecorporation.com/'

response = requests.get(url)

if response.ok:
    links=[]
    soup = BeautifulSoup(response.text,'html.parser')
    tds = soup.findAll('li')
    for td in tds:
        a =td.find('a')
        link= a['href']
        links.append(link)
    print(links)
