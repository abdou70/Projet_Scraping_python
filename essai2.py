import requests
from bs4 import BeautifulSoup
import pandas as pd

k = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky').text

soup=BeautifulSoup(k,'html.parser')

productlist = soup.find_all("li",{"class":"product-grid__item"})

print(productlist)



<li class="product-grid__item"><a class="product-card" href="/p/37325/suntory-torys-classic" onclick="_gaq.push(['_trackEvent', 'Products-GridView', 'click', '37325 : Suntory Torys Classic'])" title="Suntory Torys Classic"><div class="product-card__image-container"><img alt="Suntory Torys Classic" class="product-card__image lazy" data-original="https://img.thewhiskyexchange.com/480/japan_sun20.jpg" src="https://img.thewhiskyexchange.com/ph.png"/></div><div class="product-card__content"><p class="product-card__name"> Suntory Torys Classic </p><p class="product-card__meta"> 70cl / 37% </p></div><div class="product-card__data">
<p class="product-card__price"> \xa330.45 </p><p class="product-card__unit-price"> (\xa343.50 per litre) </p>
</div>
</a>
</li>