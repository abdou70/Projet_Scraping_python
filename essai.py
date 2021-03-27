import requests
from bs4 import BeautifulSoup
import pandas as pd 

url = 'https://www.w3schools.com/sql/'

response= requests.get(url)
if response.ok:
    print(response.text)