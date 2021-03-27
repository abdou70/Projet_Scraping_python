import requests
from bs4 import BeautifulSoup
import pandas as pd


baseurl = 'https://books.toscrape.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

#k = requests.get('https://books.toscrape.com/catalogue/page-1.html').text
#soup =BeautifulSoup(k,'html.parser')
#meslist=soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
#print(meslist)
#pour savoir le nombre de lien on ecrit le script __print(len(produitlink))
c=0
produitlink=[]
for x in range(1,51):
    k = requests.get('https://books.toscrape.com/catalogue/page-{}.html'.format(x)).text
    soup = BeautifulSoup(k,'html.parser')
    meslist = soup.find_all("li",{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    for produit in meslist:
        a=produit.find('a').get('href')
        produitlink.append(baseurl + a)

data=[]
for link in produitlink:
    f = requests.get(link,headers=headers).text
    hun = BeautifulSoup(f,'html.parser')


    try:
        price = hun.find("p",{"class":"price_color"}).text.replace('\n',"")
    except:
        price = None

    try:
        about = hun.find("div",{"class":"sub-header"}).text.replace('\n',"")
    except:
        about = None

    try:
        name = hun.find('h1').text.replace('\n',"")
    except:
        name = None

    film  = {"name":name,"about":about,"price":price}

    data.append(film)
    #c=c+1
    #print("completed",c)

df = pd.DataFrame(data)
print(df)